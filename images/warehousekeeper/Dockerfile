FROM docker.io/library/spark:3.5.6-scala2.12-java17-python3-ubuntu@sha256:bdbe9a1689492ca8804a9c891cdea819430f60ec2cbc2cbd9aff73b3ddee3365
WORKDIR /opt/warehousekeeper
USER root

RUN <<EOF
set -e
mkdir /home/spark
chown -R spark:spark /home/spark
wget -q -P /opt/spark/jars/ https://repo1.maven.org/maven2/io/delta/delta-spark_2.12/3.2.1/delta-spark_2.12-3.2.1.jar
wget -q -P /opt/spark/jars/ https://repo1.maven.org/maven2/io/delta/delta-storage/3.2.1/delta-storage-3.2.1.jar
wget -q -P /opt/spark/jars/ https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar
wget -q -P /opt/spark/jars/ https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar
EOF

USER 185:185

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY warehousekeeper.py .

ENV IS_RUNNING_IN_CONTAINER="true"
ENTRYPOINT [ "python3", "/opt/warehousekeeper/warehousekeeper.py" ]
CMD [ "--help" ]
