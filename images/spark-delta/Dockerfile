FROM docker.io/library/spark:3.4.1-scala2.12-java11-python3-ubuntu@sha256:6f47825b37da97567f6ec83f6317f0a4b5e766463bfe4c4149600f2e4c5c4cc6

RUN /opt/spark/bin/spark-shell -v \
    --conf "spark.driver.extraJavaOptions=-Divy.cache.dir=/tmp -Divy.home=/tmp" \
    --packages "io.delta:delta-core_2.12:2.4.0,org.apache.hadoop:hadoop-aws:3.3.1"

USER 185:185
