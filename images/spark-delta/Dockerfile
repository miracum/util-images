FROM docker.io/library/spark:3.4.1-scala2.12-java11-python3-ubuntu@sha256:c6e6c7216113eabb87e7d69d6d2fef12cf7e88eb74a907e455ea87e6f35fb5ce
ENV SPARK_JARS_IVY="/home/spark/.ivy"

USER root

RUN <<EOF
mkdir /home/spark
chown -R spark:spark /home/spark
EOF

USER 185:185

RUN <<EOF
wget -q -P /opt/spark/jars https://repo1.maven.org/maven2/io/delta/delta-core_2.12/2.4.0/delta-core_2.12-2.4.0.jar
wget -q -P /opt/spark/jars https://repo1.maven.org/maven2/io/delta/delta-storage/2.4.0/delta-storage-2.4.0.jar
wget -q -P /opt/spark/jars https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar
wget -q -P /opt/spark/jars https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar
EOF
