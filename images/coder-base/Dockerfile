# syntax=docker/dockerfile:1.7.0@sha256:dbbd5e059e8a07ff7ea6233b213b36aa516b4c53c645f1817a4dd18b83cbea56
FROM docker.io/library/ubuntu:24.04@sha256:723ad8033f109978f8c7e6421ee684efb624eb5b9251b70c6788fdb2405d050b

SHELL ["/bin/bash", "-eo", "pipefail", "-c"]
ENV LANG=en_US.UTF-8

# not set as an env var so only available during build
ARG DEBIAN_FRONTEND=noninteractive

USER root

COPY packages.txt /tmp/setup/

# hadolint ignore=DL3008
RUN <<EOF
apt-get update
xargs -r -a /tmp/setup/packages.txt apt-get install -y --no-install-recommends
apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false
apt-get clean
rm -rf /var/lib/apt/lists/*

echo "ca_certificate=/etc/ssl/certs/ca-certificates.crt" >> /etc/wgetrc

useradd coder --create-home --shell=/bin/bash --uid=10001 --user-group
EOF

# Spark
RUN <<EOF
curl -LSsO https://dlcdn.apache.org/spark/spark-3.4.2/spark-3.4.2-bin-hadoop3.tgz
tar xvf spark-3.4.2-bin-hadoop3.tgz
mv spark-3.4.2-bin-hadoop3 /opt/spark
rm spark-3.4.2-bin-hadoop3.tgz

curl -LSsO --output-dir /opt/spark/jars https://repo1.maven.org/maven2/io/delta/delta-core_2.12/2.4.0/delta-core_2.12-2.4.0.jar
curl -LSsO --output-dir /opt/spark/jars https://repo1.maven.org/maven2/io/delta/delta-storage/2.4.0/delta-storage-2.4.0.jar
curl -LSsO --output-dir /opt/spark/jars https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar
curl -LSsO --output-dir /opt/spark/jars https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar
curl -LSsO --output-dir /opt/spark/jars https://repo1.maven.org/maven2/au/csiro/pathling/library-runtime/6.4.2/library-runtime-6.4.2.jar
# curl -LSsO --output-dir /opt/spark/jars https://github.com/apache/incubator-gluten/releases/download/v1.1.1/gluten-velox-bundle-spark3.3_2.12-1.1.1.jar
EOF

# DuckDB
RUN <<EOF
curl -LSsO https://github.com/duckdb/duckdb/releases/download/v0.10.1/duckdb_cli-linux-amd64.zip
unzip duckdb_cli-linux-amd64.zip
mv duckdb /usr/local/bin
duckdb --version
EOF

# MinIO client
RUN <<EOF
curl https://dl.min.io/client/mc/release/linux-amd64/mc -o /usr/local/bin/mc
chmod +x /usr/local/bin/mc
EOF

# kubectl
COPY --from=docker.io/bitnami/kubectl:1.29.3@sha256:030eecfae01810d0b0930a809532159554e4e263fd38afcefb5ee45bd014b75e /opt/bitnami/kubectl/bin/kubectl /usr/local/bin/kubectl
RUN kubectl version --client

# Helm
# renovate: datasource=github-releases depName=helm/helm
ARG HELM_VERSION=3.14.3
ENV HELM_URL=https://get.helm.sh/helm-v"${HELM_VERSION}"-linux-amd64.tar.gz
RUN <<EOF
curl -LSs "$HELM_URL" | tar xz
mv linux-amd64/helm /usr/local/bin/helm
chmod +x /usr/local/bin/helm
helm version
EOF

# cosign
# renovate: datasource=github-releases depName=sigstore/cosign
ARG COSIGN_VERSION=2.2.3
ENV COSIGN_URL=https://github.com/sigstore/cosign/releases/download/v${COSIGN_VERSION}/cosign-linux-amd64
RUN <<EOF
curl -LSsO "$COSIGN_URL"
mv ./cosign-linux-amd64 /usr/local/bin/cosign
chmod +x /usr/local/bin/cosign
cosign version
EOF

# crane
# renovate: datasource=github-releases depName=google/go-containerregistry
ARG CRANE_VERSION=0.19.1
ENV CRANE_URL=https://github.com/google/go-containerregistry/releases/download/v${CRANE_VERSION}/go-containerregistry_Linux_x86_64.tar.gz
RUN <<EOF
curl -LSs "$CRANE_URL" | tar xz
mv ./crane /usr/local/bin/crane
chmod +x /usr/local/bin/crane
crane version
EOF

ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin
WORKDIR /home/coder
USER 10001:10001
