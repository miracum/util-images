FROM docker.io/cricketeerone/apache-kafka-connect:4.0.0-confluent-hub@sha256:15454efc2dcff3e94317837f5fa72c02d10ec3d55faff4946929d1bc23bf4b26
SHELL ["/bin/bash", "-eo", "pipefail", "-c"]

ARG CONFLUENT_CONNECT_TRANSFORMS_VERSION=1.6.2
ARG CONFLUENT_KAFKA_CONNECT_JDBC_PLUGIN_VERSION=10.9.2

# renovate: datasource=maven depName=com.mysql:mysql-connector-j
ARG MYSQL_JDBC_VERSION=9.5.0
# renovate: datasource=maven depName=org.mariadb.jdbc:mariadb-java-client
ARG MARIADB_JDBC_VERSION=3.5.7
# renovate: datasource=maven depName=com.oracle.database.jdbc:ojdbc11
ARG ORACLE_OJDBC_VERSION=23.26.0.0.0
# renovate: datasource=maven depName=com.microsoft.sqlserver:mssql-jdbc
ARG MSSQL_JDBC_VERSION=13.2.1.jre11
# renovate: datasource=maven depName=io.trino:trino-jdbc
ARG TRINO_JDBC_VERSION=479
# renovate: datasource=maven depName=org.postgresql:postgresql
ARG POSTGRESQL_VERSION=42.7.7

WORKDIR /app/libs/

RUN <<EOF
confluent-hub install --no-prompt \
    --component-dir /app/libs --worker-configs /app/resources/connect-distributed.properties -- \
    confluentinc/kafka-connect-jdbc:${CONFLUENT_KAFKA_CONNECT_JDBC_PLUGIN_VERSION}

confluent-hub install --no-prompt \
    --component-dir /app/libs --worker-configs /app/resources/connect-distributed.properties -- \
    confluentinc/connect-transforms:${CONFLUENT_CONNECT_TRANSFORMS_VERSION}
EOF

WORKDIR /app/libs/confluentinc-kafka-connect-jdbc/lib/

RUN <<EOF
curl -fLsSO https://repo1.maven.org/maven2/com/mysql/mysql-connector-j/${MYSQL_JDBC_VERSION}/mysql-connector-j-${MYSQL_JDBC_VERSION}.jar
curl -fLsSO https://repo1.maven.org/maven2/org/mariadb/jdbc/mariadb-java-client/${MARIADB_JDBC_VERSION}/mariadb-java-client-${MARIADB_JDBC_VERSION}.jar
curl -fLsSO https://repo1.maven.org/maven2/com/oracle/database/jdbc/ojdbc11/${ORACLE_OJDBC_VERSION}/ojdbc11-${ORACLE_OJDBC_VERSION}.jar
curl -fLsSO https://repo1.maven.org/maven2/org/postgresql/postgresql/${POSTGRESQL_VERSION}/postgresql-${POSTGRESQL_VERSION}.jar
curl -fLsSO https://repo1.maven.org/maven2/io/trino/trino-jdbc/${TRINO_JDBC_VERSION}/trino-jdbc-${TRINO_JDBC_VERSION}.jar
curl -fLsSO https://repo1.maven.org/maven2/com/microsoft/sqlserver/mssql-jdbc/${MSSQL_JDBC_VERSION}/mssql-jdbc-${MSSQL_JDBC_VERSION}.jar  
EOF

WORKDIR /
USER 65534:65534
