FROM docker.io/apache/kyuubi:1.9.0-spark@sha256:6b7e8205e6c744d7ff52691156e315aea085c41a3d1b715c5918e1c44d0b8ed3

RUN <<EOF
wget -q -P /opt/kyuubi/externals/spark-*/jars https://repo1.maven.org/maven2/io/delta/delta-spark_2.12/3.2.0/delta-spark_2.12-3.2.0.jar
wget -q -P /opt/kyuubi/externals/spark-*/jars https://repo1.maven.org/maven2/io/delta/delta-storage/3.2.0/delta-storage-3.2.0.jar
wget -q -P /opt/kyuubi/externals/spark-*/jars https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar
wget -q -P /opt/kyuubi/externals/spark-*/jars https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar

wget -q -P /opt/kyuubi/jars "https://repo1.maven.org/maven2/org/postgresql/postgresql/42.7.3/postgresql-42.7.3.jar"
EOF

USER 10009:0
