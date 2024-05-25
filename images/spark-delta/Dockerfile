FROM docker.io/library/spark:3.5.1-scala2.12-java17-python3-ubuntu@sha256:39773ed729461cc75078376096cc96149895e800e347b0042f12d87b0130aa08
USER root

RUN <<EOF
mkdir /home/spark
chown -R spark:spark /home/spark
EOF

USER 185:185

RUN <<EOF
wget -q -P /opt/spark/jars https://repo1.maven.org/maven2/io/delta/delta-spark_2.12/3.2.0/delta-spark_2.12-3.2.0.jar
wget -q -P /opt/spark/jars https://repo1.maven.org/maven2/io/delta/delta-storage/3.2.0/delta-storage-3.2.0.jar
wget -q -P /opt/spark/jars https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.4.0/hadoop-aws-3.4.0.jar
wget -q -P /opt/spark/jars https://repo1.maven.org/maven2/software/amazon/awssdk/bundle/2.23.19/bundle-2.23.19.jar
EOF
