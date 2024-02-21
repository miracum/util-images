FROM docker.io/jupyter/all-spark-notebook:spark-3.4.1@sha256:ca30ccd3a45ab2746bd602c12a89c9d311c8e81825fe94e17f0b7835d3335849

USER 0

RUN <<EOF
wget -q -P /usr/local/spark/jars/ https://repo1.maven.org/maven2/io/delta/delta-core_2.12/2.4.0/delta-core_2.12-2.4.0.jar
wget -q -P /usr/local/spark/jars/ https://repo1.maven.org/maven2/io/delta/delta-storage/2.4.0/delta-storage-2.4.0.jar
wget -q -P /usr/local/spark/jars/ https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar
wget -q -P /usr/local/spark/jars/ https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar
EOF

USER 1000:100
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
