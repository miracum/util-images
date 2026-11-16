FROM ghcr.io/omnigent-ai/omnigent-host:v0.21.0@sha256:da9265d28a920d876c89d464b599d4bdcf4647bc338e3c4f79e3e2714570c7e5
SHELL ["/bin/bash", "-eo", "pipefail", "-c"]
ENV SDKMAN_DIR="/usr/local/sdkman" \
    PATH="$PATH:/usr/local/sdkman/bin"

# not set as an env var so only available during build
ARG DEBIAN_FRONTEND=noninteractive

# the upstream image already ships curl, unzip, and git. `zip` is required by the SDKMAN installer.
# hadolint ignore=DL3008
RUN <<EOF
apt-get update
apt-get install -y --no-install-recommends zip
apt-get clean
rm -rf /var/lib/apt/lists/*
EOF

WORKDIR /tmp/setup

# DuckDB
# renovate: datasource=github-releases depName=duckdb/duckdb
ARG DUCKDB_VERSION=1.5.6
ENV DUCKDB_URL=https://github.com/duckdb/duckdb/releases/download/v${DUCKDB_VERSION}/duckdb_cli-linux-amd64.zip
RUN <<EOF
curl -fLSsO "$DUCKDB_URL"
unzip duckdb_cli-linux-amd64.zip
mv duckdb /usr/local/bin/duckdb
rm duckdb_cli-linux-amd64.zip
duckdb --version
EOF

# AWS CLI v2
# renovate: datasource=github-tags depName=aws/aws-cli extractVersion=^(?<version>.*)$
ARG AWS_CLI_VERSION=2.39.0
ENV AWS_CLI_URL=https://awscli.amazonaws.com/awscli-exe-linux-x86_64-${AWS_CLI_VERSION}.zip
RUN <<EOF
curl -fLSs "$AWS_CLI_URL" -o awscliv2.zip
unzip -q awscliv2.zip
./aws/install --install-dir /usr/local/aws-cli --bin-dir /usr/local/bin
rm -rf awscliv2.zip aws
aws --version
EOF

# kubectl
COPY --from=docker.io/rancher/kubectl:v1.36.2@sha256:06c7a7a9772737494ae1e0c3af90f1b5385630c147e47c1c7cea92f4bed55fbe /bin/kubectl /usr/local/bin/kubectl
RUN kubectl version --client

# Helm
# renovate: datasource=github-releases depName=helm/helm
ARG HELM_VERSION=4.3.1
ENV HELM_URL=https://get.helm.sh/helm-v"${HELM_VERSION}"-linux-amd64.tar.gz
RUN <<EOF
curl -fLSs "$HELM_URL" | tar xz
mv linux-amd64/helm /usr/local/bin/helm
chmod +x /usr/local/bin/helm
rm -rf linux-amd64
helm version
EOF

# crane
# renovate: datasource=github-releases depName=google/go-containerregistry
ARG CRANE_VERSION=0.22.1
ENV CRANE_URL=https://github.com/google/go-containerregistry/releases/download/v${CRANE_VERSION}/go-containerregistry_Linux_x86_64.tar.gz
RUN <<EOF
curl -fLSs "$CRANE_URL" | tar xz crane
mv ./crane /usr/local/bin/crane
chmod +x /usr/local/bin/crane
crane version
EOF

# uv
COPY --from=ghcr.io/astral-sh/uv:0.13.6@sha256:af22a52f5eafef3d78e551599d405c02df61919d18028f0cea8eda93bc9986d0 /uv /uvx /usr/local/bin/
RUN uv --version

# SDKMAN, installed globally, with Java 17, 21, and 25 pre-installed and 21 as the default. Owned by the upstream
# `sandbox` user (uid/gid 1000660000) the host runs as on Kubernetes, so agents can `sdk install` candidates at
# runtime. HOME is an emptyDir there, so the init script is hooked into the system-wide shell configuration
# instead of ~/.bashrc. The default Java is also put on the PATH via ENV so it is available in non-interactive
# shells that never source the init script.
# SDKMAN only serves the latest patch release per major version, so these must be bumped once they disappear.
ARG JAVA_17_VERSION=17.0.21.0+9-tem
ARG JAVA_21_VERSION=21.0.13.0+9-tem
ARG JAVA_25_VERSION=25.0.5.0+8-tem
# hadolint ignore=SC2016
RUN <<EOF
curl -fsSL "https://get.sdkman.io?ci=true&rcupdate=false" | bash
. "${SDKMAN_DIR}/bin/sdkman-init.sh"
sdk version
echo "n" | sdk install java "${JAVA_17_VERSION}"
echo "n" | sdk install java "${JAVA_25_VERSION}"
echo "n" | sdk install java "${JAVA_21_VERSION}"
sdk default java "${JAVA_21_VERSION}"
sdk flush tmp
chown -R sandbox:sandbox "${SDKMAN_DIR}"
echo '[[ -s "/usr/local/sdkman/bin/sdkman-init.sh" ]] && . "/usr/local/sdkman/bin/sdkman-init.sh"' > /etc/profile.d/sdkman.sh
echo '[[ -s "/usr/local/sdkman/bin/sdkman-init.sh" ]] && . "/usr/local/sdkman/bin/sdkman-init.sh"' >> /etc/bash.bashrc
EOF

# only set after the installation: SDKMAN fails if the PATH references the not yet existing `current` candidate
ENV JAVA_HOME="${SDKMAN_DIR}/candidates/java/current"
ENV PATH="$PATH:${JAVA_HOME}/bin"
RUN java --version

# Trino CLI, uses the default Java from above
# renovate: datasource=github-releases depName=trinodb/trino extractVersion=^(?<version>.*)$ versioning=loose
ARG TRINO_CLI_VERSION=484
ENV TRINO_CLI_URL=https://github.com/trinodb/trino/releases/download/${TRINO_CLI_VERSION}/trino-cli-${TRINO_CLI_VERSION}
RUN <<EOF
curl -fLSs "$TRINO_CLI_URL" -o /usr/local/bin/trino
chmod +x /usr/local/bin/trino
trino --version
EOF

# the upstream image runs as root. Use its `sandbox` user instead, the same identity upstream's Kubernetes
# sandbox launcher runs host Pods as.
WORKDIR /sandbox
USER 1000660000:1000660000
