FROM docker.io/apache/kyuubi:1.8.0-spark@sha256:eb8dbc7a475207710ee45ef14c19f673d2d10e2ad909881ff0c7fb6b2c9b50f4

RUN <<EOF
wget -q -P /opt/kyuubi/externals/spark-3.4.1-bin-hadoop3/jars https://repo1.maven.org/maven2/io/delta/delta-core_2.12/2.4.0/delta-core_2.12-2.4.0.jar
wget -q -P /opt/kyuubi/externals/spark-3.4.1-bin-hadoop3/jars https://repo1.maven.org/maven2/io/delta/delta-storage/2.4.0/delta-storage-2.4.0.jar
wget -q -P /opt/kyuubi/externals/spark-3.4.1-bin-hadoop3/jars https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar
wget -q -P /opt/kyuubi/externals/spark-3.4.1-bin-hadoop3/jars https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar
EOF

USER 10009:0
