FROM docker.io/curlimages/curl:8.22.0@sha256:58adaa4e8dca9c988bae2aba4ab3434a0bb2da16bbe3f92dec39ec7785166777 AS downloader
SHELL ["/bin/sh", "-eo", "pipefail", "-c"]
WORKDIR /tmp/libs
# the Delta Lake version should match the one used by Pathling (`pathling.deltaVersion` in <https://github.com/aehrc/pathling/blob/main/pom.xml>)
RUN <<EOF
curl -fLsSO "https://repo1.maven.org/maven2/io/delta/delta-spark_2.13/4.0.0/delta-spark_2.13-4.0.0.jar"
curl -fLsSO "https://repo1.maven.org/maven2/io/delta/delta-storage/4.0.0/delta-storage-4.0.0.jar"
curl -fLsSO "https://repo1.maven.org/maven2/org/postgresql/postgresql/42.7.13/postgresql-42.7.13.jar"
# hadoop-yarn-api and hadoop-yarn-common are stripped from the standalone-metastore base image, but the metastore's
# HiveProtoEventsCleanerTask needs `org.apache.hadoop.yarn.util.SystemClock`. Without them, none of the "always"
# housekeeping tasks start and the log shows `NoClassDefFoundError: org/apache/hadoop/yarn/util/SystemClock`.
curl -fLsSO "https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-yarn-api/3.4.1/hadoop-yarn-api-3.4.1.jar"
curl -fLsSO "https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-yarn-common/3.4.1/hadoop-yarn-common-3.4.1.jar"
EOF

# The standalone-metastore base image ships hadoop-aws but not the AWS SDK v2 it needs, nor the 560MB `bundle` artifact.
# Instead of adding the bundle back, only the S3 modules and their dependencies are resolved, see pom.xml.
# Netty, Apache HttpClient, commons-* and SLF4J are excluded since the base image already contains the exact same versions.
FROM docker.io/library/maven:3-eclipse-temurin-21@sha256:9b4877723dadf350b452dd97d9a6401e7b56f98fa9dfe420c32ad909989c7e4c AS aws-sdk
WORKDIR /build
COPY pom.xml .
RUN mvn --batch-mode --quiet dependency:copy-dependencies \
  -DoutputDirectory=/libs \
  -DincludeScope=runtime \
  -DexcludeGroupIds=io.netty,org.slf4j,commons-codec,commons-logging,org.apache.httpcomponents

# The standalone-metastore variant only contains the metastore service, without Tez, HiveServer2, beeline, etc.,
# which makes it much smaller than the full `apache/hive` image. Ships with Hadoop 3.4.1, the same version used by
# Pathling (`pathling.hadoopVersion`).
# Its entrypoint only regenerates `metastore-site.xml` and `core-site.xml`, a mounted `hive-site.xml` is left alone.
FROM docker.io/apache/hive:standalone-metastore-4.2.1@sha256:f11de992645702a028bf514e3d23400162fff65e7480dad9722b9ef78cdc6142
SHELL ["/bin/bash", "-eo", "pipefail", "-c"]
USER 0

# Ususally, upgrading all packages is a bad idea in Container images as it causes image builds to become non-reproducible.
# Unfortunately, the base image is not regularly updated, so we need to do this to get the latest security updates.
# hadoop-aws is already part of the base image's Hadoop distribution, it just isn't on Hive's classpath by default.
# Linking it keeps it in sync with Hadoop.
# hadolint ignore=DL3041
RUN <<EOF
microdnf upgrade -y
microdnf clean all
test -f "${HADOOP_HOME}/share/hadoop/tools/lib/hadoop-aws-3.4.1.jar"
ln -s "${HADOOP_HOME}/share/hadoop/tools/lib/hadoop-aws-3.4.1.jar" "${HIVE_HOME}/lib/hadoop-aws-3.4.1.jar"
EOF

COPY --from=downloader --chown=0:0 /tmp/libs/*.jar /opt/hive/lib/
COPY --from=aws-sdk --chown=0:0 /libs/*.jar /opt/hive/lib/
USER 1000:1000
