FROM docker.io/apache/kyuubi:1.8.2-spark@sha256:cf0513299a7d36304471fdf7ebf1d6695676005c5949da649a80f86638299acf

RUN <<EOF
wget -q -P /opt/kyuubi/externals/spark-*/jars https://repo1.maven.org/maven2/io/delta/delta-core_2.12/2.4.0/delta-core_2.12-2.4.0.jar
wget -q -P /opt/kyuubi/externals/spark-*/jars https://repo1.maven.org/maven2/io/delta/delta-storage/2.4.0/delta-storage-2.4.0.jar
wget -q -P /opt/kyuubi/externals/spark-*/jars https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar
wget -q -P /opt/kyuubi/externals/spark-*/jars https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar
EOF

USER 10009:0
