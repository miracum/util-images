FROM docker.io/library/spark:3.4.1-scala2.12-java11-python3-ubuntu@sha256:69fb485a0bcad88f9a2bf066e1b5d555f818126dc9df5a0b7e6a3b6d364bc694

USER root

RUN <<EOF
mkdir /home/spark
chown -R spark:spark /home/spark
EOF

USER 185:185

RUN <<EOF
/opt/spark/bin/spark-shell -v --packages "io.delta:delta-core_2.12:2.4.0,org.apache.hadoop:hadoop-aws:3.3.4"

# necessary for thrift server. still need to figure out why.
wget -P /opt/spark/jars https://repo1.maven.org/maven2/io/delta/delta-core_2.12/2.4.0/delta-core_2.12-2.4.0.jar
wget -P /opt/spark/jars https://repo1.maven.org/maven2/io/delta/delta-storage/2.4.0/delta-storage-2.4.0.jar
EOF
