FROM ghcr.io/omnigent-ai/omnigent-host:v0.23.0@sha256:78a05d1443fb01f5a67f8a3796427c851358386d220875a0a03533166c1ce78d
SHELL ["/bin/bash", "-eo", "pipefail", "-c"]
ENV SDKMAN_DIR="/usr/local/sdkman" \
    PATH="$PATH:/usr/local/sdkman/bin"

# not set as an env var so only available during build
ARG DEBIAN_FRONTEND=noninteractive

# the upstream image already ships curl, unzip, and git. `zip` is required by the SDKMAN installer.
# build-essential is included so pip/npm packages with native extensions can be built.
# hadolint ignore=DL3008
RUN <<EOF
apt-get update
apt-get install -y --no-install-recommends \
  zip \
  jq \
  ripgrep \
  git-lfs \
  less \
  tree \
  wget \
  shellcheck \
  build-essential
apt-get clean
rm -rf /var/lib/apt/lists/*
EOF

WORKDIR /tmp/setup

# DuckDB
# renovate: datasource=github-releases depName=duckdb/duckdb
ARG DUCKDB_VERSION=2.0.0
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
ARG AWS_CLI_VERSION=2.41.0
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

# yq
# renovate: datasource=github-releases depName=mikefarah/yq
ARG YQ_VERSION=4.54.3
ENV YQ_URL=https://github.com/mikefarah/yq/releases/download/v${YQ_VERSION}/yq_linux_amd64
RUN <<EOF
curl -fLSs "$YQ_URL" -o /usr/local/bin/yq
chmod +x /usr/local/bin/yq
yq --version
EOF

# kustomize
# renovate: datasource=github-releases depName=kubernetes-sigs/kustomize extractVersion=^kustomize/v(?<version>.*)$
ARG KUSTOMIZE_VERSION=5.8.3
ENV KUSTOMIZE_URL=https://github.com/kubernetes-sigs/kustomize/releases/download/kustomize/v${KUSTOMIZE_VERSION}/kustomize_v${KUSTOMIZE_VERSION}_linux_amd64.tar.gz
RUN <<EOF
curl -fLSs "$KUSTOMIZE_URL" | tar xz -C /usr/local/bin kustomize
chmod +x /usr/local/bin/kustomize
kustomize version
EOF

# skaffold
# renovate: datasource=github-releases depName=GoogleContainerTools/skaffold
ARG SKAFFOLD_VERSION=2.25.0
ENV SKAFFOLD_URL=https://github.com/GoogleContainerTools/skaffold/releases/download/v${SKAFFOLD_VERSION}/skaffold-linux-amd64
RUN <<EOF
curl -fLSs "$SKAFFOLD_URL" -o /usr/local/bin/skaffold
chmod +x /usr/local/bin/skaffold
skaffold version
EOF

# cosign
# renovate: datasource=github-releases depName=sigstore/cosign
ARG COSIGN_VERSION=3.1.4
ENV COSIGN_URL=https://github.com/sigstore/cosign/releases/download/v${COSIGN_VERSION}/cosign-linux-amd64
RUN <<EOF
curl -fLSs "$COSIGN_URL" -o /usr/local/bin/cosign
chmod +x /usr/local/bin/cosign
cosign version
EOF

# s5cmd
# renovate: datasource=github-releases depName=peak/s5cmd
ARG S5CMD_VERSION=2.3.0
ENV S5CMD_URL=https://github.com/peak/s5cmd/releases/download/v${S5CMD_VERSION}/s5cmd_${S5CMD_VERSION}_linux_amd64.deb
RUN <<EOF
curl -fLSsO "$S5CMD_URL"
dpkg --install "s5cmd_${S5CMD_VERSION}_linux_amd64.deb"
rm "s5cmd_${S5CMD_VERSION}_linux_amd64.deb"
s5cmd version
EOF

# Argo Workflows CLI
# renovate: datasource=github-releases depName=argoproj/argo-workflows
ARG ARGO_VERSION=4.1.6
ENV ARGO_URL=https://github.com/argoproj/argo-workflows/releases/download/v${ARGO_VERSION}/argo-linux-amd64.gz
RUN <<EOF
curl -fLSs "$ARGO_URL" | gunzip > /usr/local/bin/argo
chmod +x /usr/local/bin/argo
argo version
EOF

# Argo CD CLI
# renovate: datasource=github-releases depName=argoproj/argo-cd
ARG ARGOCD_VERSION=3.6.2
ENV ARGOCD_URL=https://github.com/argoproj/argo-cd/releases/download/v${ARGOCD_VERSION}/argocd-linux-amd64
RUN <<EOF
curl -fLSs "$ARGOCD_URL" -o /usr/local/bin/argocd
chmod +x /usr/local/bin/argocd
argocd version --client
EOF

# GitLab CLI
# renovate: datasource=gitlab-releases depName=gitlab-org/cli
ARG GLAB_VERSION=1.131.0
ENV GLAB_URL=https://gitlab.com/gitlab-org/cli/-/releases/v${GLAB_VERSION}/downloads/glab_${GLAB_VERSION}_linux_amd64.tar.gz
RUN <<EOF
curl -fLSs "$GLAB_URL" | tar xz bin/glab
mv ./bin/glab /usr/local/bin/glab
chmod +x /usr/local/bin/glab
rm -rf bin
glab --version
gh --version
EOF

# uv
COPY --from=ghcr.io/astral-sh/uv:0.13.10@sha256:a3ea1357342c1a4bf9a0c53a3deb1b55379aefa037338d8113d5771efa01774f /uv /uvx /usr/local/bin/
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
# SDKMAN_DIR is set explicitly: omnigent starts terminals without the image's ENV, and sdkman-init.sh would
# otherwise fall back to the not existing ~/.sdkman
cat > /etc/profile.d/sdkman.sh <<'SH'
export SDKMAN_DIR="/usr/local/sdkman"
[[ -s "${SDKMAN_DIR}/bin/sdkman-init.sh" ]] && . "${SDKMAN_DIR}/bin/sdkman-init.sh"
SH
echo '. /etc/profile.d/sdkman.sh' >> /etc/bash.bashrc
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
