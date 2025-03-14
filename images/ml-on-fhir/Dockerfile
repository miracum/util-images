FROM docker.io/rocker/binder:4.4.2@sha256:4b2c5045000173a166ed0e69b830de8699aadae33abde559f3abd647dab0c7d2
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
ARG NB_UID=1000 \
    NB_GID=100
USER 0

# hadolint ignore=DL3008
RUN <<EOF
apt-get -y update
apt-get install --no-install-recommends -y openjdk-17-jre-headless ca-certificates-java
rm -rf /var/lib/apt/lists/*
EOF

WORKDIR /tmp

ENV SPARK_VERSION=3.5.5 \
    HADOOP_VERSION=3

# hadolint ignore=SC2046
RUN <<EOF
wget -q "https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop3.tgz"
echo "ec5ff678136b1ff981e396d1f7b5dfbf399439c5cb853917e8c954723194857607494a89b7e205fce988ec48b1590b5caeae3b18e1b5db1370c0522b256ff376 *spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" | sha512sum -c - && \
tar xzf "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" -C /usr/local --owner root --group root --no-same-owner && \
rm "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz"
EOF

WORKDIR /usr/local
RUN ln -s "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}" spark

# Configure Spark
ENV SPARK_HOME=/usr/local/spark
ENV PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.9-src.zip \
    SPARK_OPTS="--driver-java-options=-Dlog4j.logLevel=info" \
    PATH=$PATH:$SPARK_HOME/bin

RUN <<EOF
wget -q -P /usr/local/spark/jars/ "https://repo1.maven.org/maven2/io/delta/delta-spark_2.12/3.3.0/delta-spark_2.12-3.3.0.jar"
wget -q -P /usr/local/spark/jars/ "https://repo1.maven.org/maven2/io/delta/delta-storage/3.3.0/delta-storage-3.3.0.jar"
wget -q -P /usr/local/spark/jars/ "https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar"
wget -q -P /usr/local/spark/jars/ "https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar"
EOF

COPY --chown=${NB_UID}:${NB_GID} requirements.txt /tmp/
RUN pip install --no-cache-dir --requirement /tmp/requirements.txt

USER ${NB_UID}:${NB_GID}
WORKDIR /home/${NB_USER}
