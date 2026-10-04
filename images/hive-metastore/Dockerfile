FROM docker.io/curlimages/curl:8.21.0@sha256:7c12af72ceb38b7432ab85e1a265cff6ae58e06f95539d539b654f2cfa64bb13 AS downloader
SHELL ["/bin/sh", "-eo", "pipefail", "-c"]
WORKDIR /tmp/libs
# the Delta Lake version should match the one used by Pathling (`pathling.deltaVersion` in <https://github.com/aehrc/pathling/blob/main/pom.xml>)
RUN <<EOF
curl -fLsSO "https://repo1.maven.org/maven2/io/delta/delta-spark_2.13/4.0.0/delta-spark_2.13-4.0.0.jar"
curl -fLsSO "https://repo1.maven.org/maven2/io/delta/delta-storage/4.0.0/delta-storage-4.0.0.jar"
curl -fLsSO "https://repo1.maven.org/maven2/org/postgresql/postgresql/42.7.13/postgresql-42.7.13.jar"
EOF

# ships with Hadoop 3.4.1, the same version used by Pathling (`pathling.hadoopVersion`).
# Hive 4.2.x is not used since its entrypoint always overwrites the hive-site.xml with its own template.
FROM docker.io/apache/hive:4.1.0@sha256:b957bb0e698e560d24e162b7549d79f191d58703e92899a886618c317f6e8f30
SHELL ["/bin/bash", "-eo", "pipefail", "-c"]
USER 0

# Ususally, upgrading all packages is a bad idea in Container images as it causes image builds to become non-reproducible.
# Unfortunately, the base image is not regularly updated, so we need to do this to get the latest security updates.
# hadoop-aws and the AWS SDK v2 bundle it is built against are already part of the base image's Hadoop distribution,
# they just aren't on Hive's classpath by default. Linking them keeps them in sync with Hadoop and avoids
# duplicating the ~560MB SDK bundle.
# hadolint ignore=DL3041
RUN <<EOF
# allows writing the hive-site.xml at runtime
chown -R 1000:1000 "${HIVE_HOME}/conf"
microdnf upgrade -y
microdnf install -y gettext
microdnf clean all
for jar in hadoop-aws-3.4.1.jar bundle-2.24.6.jar; do
  test -f "${HADOOP_HOME}/share/hadoop/tools/lib/${jar}"
  ln -s "${HADOOP_HOME}/share/hadoop/tools/lib/${jar}" "${HIVE_HOME}/lib/${jar}"
done
EOF

COPY --from=downloader --chown=0:0 /tmp/libs/*.jar /opt/hive/lib/
USER 1000:1000
