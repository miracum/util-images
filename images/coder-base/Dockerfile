# syntax=docker/dockerfile:1.9.0@sha256:fe40cf4e92cd0c467be2cfc30657a680ae2398318afd50b0c80585784c604f28
FROM docker.io/library/ubuntu:24.04@sha256:8a37d68f4f73ebf3d4efafbcf66379bf3728902a8038616808f04e34a9ab63ee

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
curl -LSsO https://archive.apache.org/dist/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz
tar xvf spark-3.5.1-bin-hadoop3.tgz
mv spark-3.5.1-bin-hadoop3 /opt/spark
rm spark-3.5.1-bin-hadoop3.tgz

curl -LSsO --output-dir /opt/spark/jars https://repo1.maven.org/maven2/io/delta/delta-spark_2.12/3.2.0/delta-spark_2.12-3.2.0.jar
curl -LSsO --output-dir /opt/spark/jars https://repo1.maven.org/maven2/io/delta/delta-storage/3.2.0/delta-storage-3.2.0.jar
curl -LSsO --output-dir /opt/spark/jars https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar
curl -LSsO --output-dir /opt/spark/jars https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar
curl -LSsO --output-dir /opt/spark/jars https://repo1.maven.org/maven2/au/csiro/pathling/library-runtime/7.0.1/library-runtime-7.0.1.jar
# curl -LSsO --output-dir /opt/spark/jars https://github.com/apache/incubator-gluten/releases/download/v1.1.1/gluten-velox-bundle-spark3.3_2.12-1.1.1.jar
EOF

# DuckDB
# renovate: datasource=github-releases depName=duckdb/duckdb
ARG DUCKDB_VERSION=1.0.0
ENV DUCKDB_URL=https://github.com/duckdb/duckdb/releases/download/v${DUCKDB_VERSION}/duckdb_cli-linux-amd64.zip
RUN <<EOF
curl -LSsO ${DUCKDB_URL}
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
COPY --from=docker.io/bitnami/kubectl:1.30.3@sha256:fc6e48522aa4417275d6fa92bd820f426bbf27454c80b327c449ef6e32467bd3 /opt/bitnami/kubectl/bin/kubectl /usr/local/bin/kubectl
RUN kubectl version --client

# Helm
# renovate: datasource=github-releases depName=helm/helm
ARG HELM_VERSION=3.15.3
ENV HELM_URL=https://get.helm.sh/helm-v"${HELM_VERSION}"-linux-amd64.tar.gz
RUN <<EOF
curl -LSs "$HELM_URL" | tar xz
mv linux-amd64/helm /usr/local/bin/helm
chmod +x /usr/local/bin/helm
helm version
EOF

# cosign
# renovate: datasource=github-releases depName=sigstore/cosign
ARG COSIGN_VERSION=2.3.0
ENV COSIGN_URL=https://github.com/sigstore/cosign/releases/download/v${COSIGN_VERSION}/cosign-linux-amd64
RUN <<EOF
curl -LSsO "$COSIGN_URL"
mv ./cosign-linux-amd64 /usr/local/bin/cosign
chmod +x /usr/local/bin/cosign
cosign version
EOF

# crane
# renovate: datasource=github-releases depName=google/go-containerregistry
ARG CRANE_VERSION=0.20.1
ENV CRANE_URL=https://github.com/google/go-containerregistry/releases/download/v${CRANE_VERSION}/go-containerregistry_Linux_x86_64.tar.gz
RUN <<EOF
curl -LSs "$CRANE_URL" | tar xz
mv ./crane /usr/local/bin/crane
chmod +x /usr/local/bin/crane
crane version
EOF

# s5cmd
# renovate: datasource=github-releases depName=peak/s5cmd
ARG S5CMD_VERSION=2.2.2
ENV S5CMD_URL=https://github.com/peak/s5cmd/releases/download/v${S5CMD_VERSION}/s5cmd_${S5CMD_VERSION}_linux_amd64.deb
RUN <<EOF
curl -LSsO "$S5CMD_URL"
dpkg --install s5cmd_${S5CMD_VERSION}_linux_amd64.deb
s5cmd version
EOF

ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin
WORKDIR /home/coder
USER 10001:10001
