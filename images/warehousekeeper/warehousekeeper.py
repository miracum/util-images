import os
from typing import Iterator

import boto3
import click
from deltalake import DeltaTable, WriterProperties
from loguru import logger
from pyspark.sql import SparkSession


# via https://stackoverflow.com/a/53875557
class BaseCommand(click.Command):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.params.insert(
            0,
            click.core.Option(
                ("--bucket-name",),
                type=click.STRING,
                help="name of the bucket containing the warehouse tables",
                required=True,
            ),
        )
        self.params.insert(
            1,
            click.core.Option(
                ("--database-name-prefix",),
                type=click.STRING,
                help="database name prefix in the bucket",
                required=True,
            ),
        )


spark_builder = (
    SparkSession.builder.appName("warehousekeeper")
    .config("spark.sql.catalogImplementation", "hive")
    .config(
        "spark.sql.catalog.spark_catalog",
        "org.apache.spark.sql.delta.catalog.DeltaCatalog",
    )
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config("spark.hadoop.fs.s3a.endpoint", os.getenv("AWS_ENDPOINT_URL"))
    .config("spark.hadoop.fs.s3a.path.style.access", "true")
)

# the base image already contains the below packages
# this doesn't feel like a robust solution, though...
if os.getenv("IS_RUNNING_IN_CONTAINER") is None:
    spark_builder.config(
        "spark.jars.packages",
        "io.delta:delta-spark_2.12:3.2.0,org.apache.hadoop:hadoop-aws:3.3.4",
    )


def list_tables(bucket_name: str, prefix: str) -> Iterator[DeltaTable]:
    delimiter = "/"

    logger.info(
        "Listing objects in {bucket} with prefix {prefix} delimiter {delimiter}",
        bucket=bucket_name,
        prefix=prefix,
        delimiter=delimiter,
    )

    s3_client = boto3.client("s3")
    response = s3_client.list_objects_v2(
        Bucket=bucket_name, Prefix=prefix, Delimiter=delimiter
    )

    logger.debug(response)

    if response["KeyCount"] > response["MaxKeys"]:
        logger.error(
            "Support for reading more than {max_keys} tables is not yet implemented",
            max_keys=response["MaxKeys"],
        )

    if response["KeyCount"] == 0:
        logger.warning("No objects found")
        return None

    for obj in response["CommonPrefixes"]:
        logger.debug(obj)

        table_object_name = f"s3a://{bucket_name}/{obj['Prefix']}"
        logger.info(
            "Reading table {table_object_name}", table_object_name=table_object_name
        )

        try:
            dt = DeltaTable(table_object_name)
            yield dt
        except Exception as e:
            logger.error("Failed to read table: {error}", error=e)


@click.group()
def cli():
    pass


@cli.command(cls=BaseCommand)
@click.option(
    "--retention-hours",
    default=None,
    type=click.INT,
    help="the retention threshold in hours, if none then the value from "
    + "`configuration.deletedFileRetentionDuration` is used or default "
    + "of 1 week otherwise.",
)
@click.option(
    "--dry-run",
    default=True,
    type=click.BOOL,
    help="when activated, list only the files, delete otherwise",
)
@click.option(
    "--enforce-retention-duration",
    default=True,
    type=click.BOOL,
    help="when disabled, accepts retention hours smaller than the value from "
    + "`configuration.deletedFileRetentionDuration`.",
)
def vacuum(
    bucket_name: str,
    database_name_prefix: str,
    retention_hours: int | None,
    dry_run: bool,
    enforce_retention_duration: bool,
):
    """Run VACUUM against all Delta tables in the given folder"""

    for dt in list_tables(bucket_name=bucket_name, prefix=database_name_prefix):
        logger.info(
            "VACUUMing '{table}' {metadata}", table=dt.table_uri, metadata=dt.metadata()
        )

        vacuumed_files = dt.vacuum(
            enforce_retention_duration=enforce_retention_duration,
            dry_run=dry_run,
            retention_hours=retention_hours,
        )
        dt.cleanup_metadata()

        logger.info("Deleted '{vacuumed_files}'", vacuumed_files=vacuumed_files)


@cli.command(cls=BaseCommand)
@click.option(
    "--compression-level",
    type=click.INT,
    help="The compression level to use",
    required=False,
    default=9,
)
@click.option(
    "--compression-type",
    type=click.STRING,
    help="The compression type to use",
    required=False,
    default="ZSTD",
)
def optimize(
    bucket_name: str,
    database_name_prefix: str,
    compression_type: str,
    compression_level: int,
):
    """Run OPTIMIZE against all Delta tables in the database"""

    wp = WriterProperties(
        compression=compression_type,
        compression_level=compression_level,
    )

    for dt in list_tables(bucket_name=bucket_name, prefix=database_name_prefix):
        logger.info(
            "OPTIMIZing '{table}' {metadata}",
            table=dt.table_uri,
            metadata=dt.metadata(),
        )
        metrics = dt.optimize.compact(writer_properties=wp)
        logger.info(metrics)


@cli.command(cls=BaseCommand)
@click.option(
    "--hive-metastore",
    type=click.STRING,
    help="The hive metastore URI, e.g. thrift://hive-metastore:9083",
    required=True,
)
def register(bucket_name: str, database_name_prefix: str, hive_metastore: str):
    """
    Register all Delta tables in the given folder in a Hive metastore
    using the folder as the schema name.
    """
    spark = spark_builder.config(
        "spark.hive.metastore.uris", hive_metastore
    ).getOrCreate()

    for dt in list_tables(bucket_name=bucket_name, prefix=database_name_prefix):
        logger.info(
            "Registering '{table}' {metadata} in '{metastore}'",
            table=dt.table_uri,
            metadata=dt.metadata(),
            metastore=hive_metastore,
        )

        # e.g. s3a://fhir/default/Patient.parquet
        table_path = dt.table_uri

        # the second to last part when splitting by '/' is 'default'
        schema = table_path.split("/")[-2]

        # the table path but without the table name
        schema_path = table_path.removesuffix(table_path.split("/")[-1])

        # the final folder name without the '.parquet' extension
        table_name = table_path.split("/")[-1].removesuffix(".parquet")

        # The parametrized query below didn't work due to parsing errors
        # from the '-quoted schema.
        # The working query uses Python string interpolation and is technically
        # vulnerable to SQL injection.
        # spark.sql(
        #     "CREATE SCHEMA IF NOT EXISTS {schema} LOCATION {schema_path}",
        #     schema=schema,
        #     schema_path=schema_path,
        # ).show()

        create_schema_query = (
            f"CREATE SCHEMA IF NOT EXISTS {schema} LOCATION '{schema_path}'"
        )
        logger.info(create_schema_query)
        spark.sql(create_schema_query)

        create_table_query = (
            f"CREATE TABLE IF NOT EXISTS {schema}.{table_name} "
            + f"USING DELTA LOCATION '{table_path}'"
        )
        logger.info(create_table_query)
        spark.sql(create_table_query)


if __name__ == "__main__":
    cli()
