FROM docker.io/curlimages/curl:8.12.1@sha256:94e9e444bcba979c2ea12e27ae39bee4cd10bc7041a472c4727a558e213744e6 AS downloader
WORKDIR /tmp/libs
RUN <<EOF
curl -LsSO "https://repo1.maven.org/maven2/io/delta/delta-spark_2.12/3.3.0/delta-spark_2.12-3.3.0.jar"
curl -LsSO "https://repo1.maven.org/maven2/io/delta/delta-storage/3.3.0/delta-storage-3.3.0.jar"
curl -LsSO "https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar"
curl -LsSO "https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar"
curl -LsSO "https://repo1.maven.org/maven2/org/postgresql/postgresql/42.7.5/postgresql-42.7.5.jar"
EOF

FROM docker.io/apache/hive:4.0.0@sha256:c0b241c544d341c16a6d8cafcb801a071be9b02054a5add255e9a0e826095e88
COPY --from=downloader --chown=0:0 /tmp/libs/*.jar /opt/hive/lib/
USER 1000:1000
