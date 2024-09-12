FROM docker.io/apache/kyuubi:1.9.2-spark@sha256:20eb6c48ce23829c84d00e2933e1d73aba96e776d05547c18a58f9cb6d981af4

RUN <<EOF
wget -q -P /opt/kyuubi/externals/spark-*/jars https://repo1.maven.org/maven2/io/delta/delta-spark_2.12/3.2.0/delta-spark_2.12-3.2.0.jar
wget -q -P /opt/kyuubi/externals/spark-*/jars https://repo1.maven.org/maven2/io/delta/delta-storage/3.2.0/delta-storage-3.2.0.jar
wget -q -P /opt/kyuubi/externals/spark-*/jars https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar
wget -q -P /opt/kyuubi/externals/spark-*/jars https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar

wget -q -P /opt/kyuubi/jars "https://repo1.maven.org/maven2/org/postgresql/postgresql/42.7.3/postgresql-42.7.3.jar"
EOF

USER 10009:0
