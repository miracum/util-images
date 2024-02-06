FROM docker.io/library/spark:3.4.1-scala2.12-java11-python3-ubuntu@sha256:69fb485a0bcad88f9a2bf066e1b5d555f818126dc9df5a0b7e6a3b6d364bc694

RUN /opt/spark/bin/spark-shell -v \
    --conf "spark.driver.extraJavaOptions=-Divy.cache.dir=/tmp -Divy.home=/tmp" \
    --packages "io.delta:delta-core_2.12:2.4.0,org.apache.hadoop:hadoop-aws:3.3.1"

USER 185:185
