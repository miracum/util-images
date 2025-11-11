FROM docker.io/curlimages/curl:8.17.0@sha256:935d9100e9ba842cdb060de42472c7ca90cfe9a7c96e4dacb55e79e560b3ff40 AS downloader
SHELL ["/bin/sh", "-eo", "pipefail", "-c"]
WORKDIR /tmp/libs
RUN <<EOF
curl -fLsSO "https://repo1.maven.org/maven2/io/delta/delta-spark_2.12/3.3.2/delta-spark_2.12-3.3.2.jar"
curl -fLsSO "https://repo1.maven.org/maven2/io/delta/delta-storage/3.3.2/delta-storage-3.3.2.jar"
curl -fLsSO "https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar"
curl -fLsSO "https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar"
curl -fLsSO "https://repo1.maven.org/maven2/org/postgresql/postgresql/42.7.7/postgresql-42.7.7.jar"
EOF

FROM docker.io/apache/hive:4.0.0@sha256:c0b241c544d341c16a6d8cafcb801a071be9b02054a5add255e9a0e826095e88
SHELL ["/bin/bash", "-eo", "pipefail", "-c"]
USER 0

# Ususally, apt-get update & upgrade is a bad idea in Container images as it causes image builds to become non-reproducible.
# Unfortunately, the base image is quite old and not regularly updated, so we need to do this to get the latest security updates.
# The altenative would be to use a a default Ubuntu image and install Hive manually.
# hadolint ignore=DL3008
RUN <<EOF
chown -R 1000:1000 /opt/hive
apt-get update
apt-get upgrade -y
apt-get install -y --no-install-recommends gettext-base
apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false
apt-get clean
rm -rf /var/lib/apt/lists/*
EOF

COPY --from=downloader --chown=0:0 /tmp/libs/*.jar /opt/hive/lib/
USER 1000:1000
