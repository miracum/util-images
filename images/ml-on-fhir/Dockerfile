FROM docker.io/jupyter/pyspark-notebook:spark-3.4.1@sha256:93d072568fec20e9fd63dabc8b7af5a654001644a43b882296bcbbfb60b952a6
WORKDIR /home/jovyan

USER 0

RUN <<EOF
wget -q -P /usr/local/spark/jars/ https://repo1.maven.org/maven2/io/delta/delta-spark_2.12/3.2.0/delta-spark_2.12-3.2.0.jar
wget -q -P /usr/local/spark/jars/ https://repo1.maven.org/maven2/io/delta/delta-storage/3.2.0/delta-storage-3.2.0.jar
wget -q -P /usr/local/spark/jars/ https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar
wget -q -P /usr/local/spark/jars/ https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar
EOF

COPY --chown=${NB_UID}:${NB_GID} requirements.txt /tmp/
RUN pip install --no-cache-dir --requirement /tmp/requirements.txt && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

USER ${NB_UID}:${NB_GID}
