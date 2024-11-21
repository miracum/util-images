FROM docker.io/library/spark:3.5.3-scala2.12-java17-python3-ubuntu@sha256:3d6e110ff627cd7bbf4dd10051acb3c7de6695b55cf174d20dc4b445f7f83bcd
USER root

RUN <<EOF
mkdir /home/spark
chown -R spark:spark /home/spark
EOF

USER 185:185

RUN <<EOF
wget -q -P /opt/spark/jars https://repo1.maven.org/maven2/io/delta/delta-spark_2.12/3.2.0/delta-spark_2.12-3.2.0.jar
wget -q -P /opt/spark/jars https://repo1.maven.org/maven2/io/delta/delta-storage/3.2.0/delta-storage-3.2.0.jar
wget -q -P /opt/spark/jars https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar
wget -q -P /opt/spark/jars https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar
wget -q -P /opt/spark/jars https://repo1.maven.org/maven2/org/apache/kyuubi/kyuubi-spark-sql-engine_2.12/1.9.0/kyuubi-spark-sql-engine_2.12-1.9.0.jar
EOF
