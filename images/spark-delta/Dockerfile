FROM docker.io/library/spark:3.4.1-scala2.12-java11-python3-ubuntu@sha256:3adf35b5f50409d1b3c003af911bfaa364e2694f1b849fadb7bfad811c9107c7

RUN /opt/spark/bin/spark-shell -v \
    --conf "spark.driver.extraJavaOptions=-Divy.cache.dir=/tmp -Divy.home=/tmp" \
    --packages "io.delta:delta-core_2.12:2.4.0,org.apache.hadoop:hadoop-aws:3.3.1"

USER 185:185
