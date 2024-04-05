# syntax=docker/dockerfile:1.7.0@sha256:dbbd5e059e8a07ff7ea6233b213b36aa516b4c53c645f1817a4dd18b83cbea56
FROM docker.io/library/ubuntu:24.04@sha256:723ad8033f109978f8c7e6421ee684efb624eb5b9251b70c6788fdb2405d050b

SHELL ["/bin/bash", "-eo", "pipefail", "-c"]
ENV SPARK_HOME=/opt/spark \
    PATH=$PATH:$SPARK_HOME/bin \
    LANG=en_US.UTF-8

# not set as an env var so only available during build
ARG DEBIAN_FRONTEND=noninteractive

USER root

# hadolint ignore=DL3008
RUN <<EOF
apt-get update
apt-get install -y --no-install-recommends jq zip unzip git curl wget python3 python3-pip python-is-python3

# JDK
wget -qO - https://packages.adoptium.net/artifactory/api/gpg/key/public | gpg --dearmor | tee /etc/apt/trusted.gpg.d/adoptium.gpg > /dev/null
echo "deb https://packages.adoptium.net/artifactory/deb $(awk -F= '/^VERSION_CODENAME/{print$2}' /etc/os-release) main" | tee /etc/apt/sources.list.d/adoptium.list
apt-get update
apt-get install -y --no-install-recommends temurin-17-jdk

apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false
apt-get clean
rm -rf /var/lib/apt/lists/*
echo "ca_certificate=/etc/ssl/certs/ca-certificates.crt" >> /etc/wgetrc
EOF

# Spark
RUN <<EOF
curl -LO https://dlcdn.apache.org/spark/spark-3.4.2/spark-3.4.2-bin-hadoop3.tgz
tar xvf spark-3.4.2-bin-hadoop3.tgz
sudo mv spark-3.4.0-bin-hadoop3 /opt/spark
EOF

RUN useradd coder \
    --create-home \
    --shell=/bin/bash \
    --uid=10001 \
    --user-group

USER 10001:10001
