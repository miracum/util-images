FROM docker.io/library/ubuntu:26.04@sha256:6a06111c3b0a8600feadb270aec771dc239bf407b25625f93f44ab00e11f4d3c
SHELL ["/bin/bash", "-eo", "pipefail", "-c"]
ENV LANG=en_US.UTF-8 \
    SDKMAN_DIR="/usr/local/sdkman" \
    PATH="$PATH:/usr/local/sdkman/bin/:/home/coder/.local/bin/:/usr/local/node_modules/.bin"

# not set as an env var so only available during build
ARG DEBIAN_FRONTEND=noninteractive

USER 0

COPY packages.txt /tmp/setup/

# hadolint ignore=DL3008
RUN <<EOF
apt-get update
xargs -r -a /tmp/setup/packages.txt apt-get install -y --no-install-recommends

curl -fsSL https://deb.nodesource.com/setup_24.x | bash -
apt-get install -y --no-install-recommends nodejs

apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false
apt-get clean
rm -rf /var/lib/apt/lists/*

echo "ca_certificate=/etc/ssl/certs/ca-certificates.crt" >> /etc/wgetrc

useradd coder --create-home --shell=/bin/bash --uid=10001 --user-group
EOF

# GitHub CLI
# renovate: datasource=github-releases depName=cli/cli
ARG GH_VERSION=2.105.0
ENV GH_URL=https://github.com/cli/cli/releases/download/v${GH_VERSION}/gh_${GH_VERSION}_linux_amd64.tar.gz
RUN <<EOF
curl -fLSs "$GH_URL" | tar xz --strip-components=2 -C /usr/local/bin "gh_${GH_VERSION}_linux_amd64/bin/gh"
gh --version
EOF

# GitLab CLI
# renovate: datasource=gitlab-releases depName=gitlab-org/cli
ARG GLAB_VERSION=1.131.0
ENV GLAB_URL=https://gitlab.com/gitlab-org/cli/-/releases/v${GLAB_VERSION}/downloads/glab_${GLAB_VERSION}_linux_amd64.tar.gz
RUN <<EOF
curl -fLSs "$GLAB_URL" | tar xz --strip-components=1 -C /usr/local/bin bin/glab
glab --version
EOF

# DuckDB
# renovate: datasource=github-releases depName=duckdb/duckdb
ARG DUCKDB_VERSION=2.0.0
ENV DUCKDB_URL=https://github.com/duckdb/duckdb/releases/download/v${DUCKDB_VERSION}/duckdb_cli-linux-amd64.zip
RUN <<EOF
curl -fLSsO ${DUCKDB_URL}
unzip duckdb_cli-linux-amd64.zip
mv duckdb /usr/local/bin
duckdb --version
EOF

# AWS CLI
# renovate: datasource=github-tags depName=aws/aws-cli
ARG AWS_CLI_VERSION=2.41.0
ENV AWS_CLI_URL=https://awscli.amazonaws.com/awscli-exe-linux-x86_64-${AWS_CLI_VERSION}.zip
RUN <<EOF
curl -fLSs "$AWS_CLI_URL" -o /tmp/awscliv2.zip
unzip -q /tmp/awscliv2.zip -d /tmp
/tmp/aws/install --install-dir /usr/local/aws-cli --bin-dir /usr/local/bin
rm -rf /tmp/awscliv2.zip /tmp/aws
aws --version
EOF

# kubectl
COPY --from=docker.io/rancher/kubectl:v1.36.2@sha256:06c7a7a9772737494ae1e0c3af90f1b5385630c147e47c1c7cea92f4bed55fbe /bin/kubectl /usr/local/bin/kubectl
RUN kubectl version --client

# kubectl oidc-login (kubelogin)
# renovate: datasource=github-releases depName=int128/kubelogin
ARG KUBELOGIN_VERSION=1.36.4
ENV KUBELOGIN_URL=https://github.com/int128/kubelogin/releases/download/v${KUBELOGIN_VERSION}/kubelogin_linux_amd64.zip
RUN <<EOF
curl -fLSs "$KUBELOGIN_URL" -o /tmp/kubelogin.zip
unzip -q /tmp/kubelogin.zip kubelogin -d /usr/local/bin
mv /usr/local/bin/kubelogin /usr/local/bin/kubectl-oidc_login
rm /tmp/kubelogin.zip
kubectl oidc-login --version
EOF

# Helm
# renovate: datasource=github-releases depName=helm/helm
ARG HELM_VERSION=4.3.1
ENV HELM_URL=https://get.helm.sh/helm-v"${HELM_VERSION}"-linux-amd64.tar.gz
RUN <<EOF
curl -fLSs "$HELM_URL" | tar xz
mv linux-amd64/helm /usr/local/bin/helm
chmod +x /usr/local/bin/helm
helm version
EOF

# kustomize
# renovate: datasource=github-releases depName=kubernetes-sigs/kustomize extractVersion=^kustomize/v(?<version>.*)$
ARG KUSTOMIZE_VERSION=5.8.3
ENV KUSTOMIZE_URL=https://github.com/kubernetes-sigs/kustomize/releases/download/kustomize/v${KUSTOMIZE_VERSION}/kustomize_v${KUSTOMIZE_VERSION}_linux_amd64.tar.gz
RUN <<EOF
curl -fLSs "$KUSTOMIZE_URL" | tar xz -C /usr/local/bin
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
curl -fLSsO "$COSIGN_URL"
mv ./cosign-linux-amd64 /usr/local/bin/cosign
chmod +x /usr/local/bin/cosign
cosign version
EOF

# crane
# renovate: datasource=github-releases depName=google/go-containerregistry
ARG CRANE_VERSION=0.22.1
ENV CRANE_URL=https://github.com/google/go-containerregistry/releases/download/v${CRANE_VERSION}/go-containerregistry_Linux_x86_64.tar.gz
RUN <<EOF
curl -fLSs "$CRANE_URL" | tar xz
mv ./crane /usr/local/bin/crane
chmod +x /usr/local/bin/crane
crane version
EOF

# s5cmd
# renovate: datasource=github-releases depName=peak/s5cmd
ARG S5CMD_VERSION=2.3.0
ENV S5CMD_URL=https://github.com/peak/s5cmd/releases/download/v${S5CMD_VERSION}/s5cmd_${S5CMD_VERSION}_linux_amd64.deb
RUN <<EOF
curl -fLSsO "$S5CMD_URL"
dpkg --install s5cmd_${S5CMD_VERSION}_linux_amd64.deb
s5cmd version
EOF

# Argo CLI
# renovate: datasource=github-releases depName=argoproj/argo-workflows
ARG ARGO_VERSION=4.1.6
ENV ARGO_URL=https://github.com/argoproj/argo-workflows/releases/download/v${ARGO_VERSION}/argo-linux-amd64.gz
RUN <<EOF
curl -fLSs "$ARGO_URL" | gunzip > /usr/local/bin/argo
chmod +x /usr/local/bin/argo
argo version
EOF

# code-server
# renovate: datasource=github-releases depName=coder/code-server
ARG CODE_SERVER_VERSION=4.145.2
ENV CODE_SERVER_URL=https://github.com/coder/code-server/releases/download/v${CODE_SERVER_VERSION}/code-server-${CODE_SERVER_VERSION}-linux-amd64.tar.gz
RUN <<EOF
mkdir -p /usr/local/lib/code-server
curl -fLSs "$CODE_SERVER_URL" | tar xz --strip-components=1 -C /usr/local/lib/code-server
ln -s /usr/local/lib/code-server/bin/code-server /usr/local/bin/code-server
code-server --version
EOF

# AI coding agents (crush, pi, opencode), pinned via package.json/package-lock.json
WORKDIR /usr/local
RUN --mount=type=bind,source=package.json,target=package.json \
    --mount=type=bind,source=package-lock.json,target=package-lock.json <<EOF
npm clean-install
crush --version
pi --version
opencode --version
EOF

# install uv globally
RUN <<EOF
curl -LsSf https://astral.sh/uv/install.sh | env UV_UNMANAGED_INSTALL="/usr/local/bin" sh
uv --version
EOF

# JupyterLab, in its own venv under /opt/jupyterlab.
# The venv uses --system-site-packages so the user site (~/.local, on the
# persistent home volume) is active: `%pip install` in a notebook falls back
# to a user install there and survives workspace restarts. --seed adds pip,
# which the %pip magic needs.
# renovate: datasource=pypi depName=jupyterlab
ARG JUPYTERLAB_VERSION=4.6.6
# renovate: datasource=pypi depName=ipykernel
ARG IPYKERNEL_VERSION=7.4.0
RUN <<EOF
uv venv --seed --system-site-packages --python /usr/bin/python3 /opt/jupyterlab
uv pip install --no-cache --python /opt/jupyterlab/bin/python \
  "jupyterlab==${JUPYTERLAB_VERSION}" \
  "ipykernel==${IPYKERNEL_VERSION}"
ln -s /opt/jupyterlab/bin/jupyter /opt/jupyterlab/bin/jupyter-lab /usr/local/bin/
jupyter-lab --version
EOF

# install sdkman globally
RUN <<EOF
curl -s "https://get.sdkman.io?ci=true" | bash
. "/usr/local/sdkman/bin/sdkman-init.sh"
sdk version
echo "n" | sdk install java 17.0.18-tem
echo "n" | sdk install java 21.0.9-tem
echo "n" | sdk install java 25.0.2-tem
sdk default java 21.0.9-tem
EOF

WORKDIR /home/coder
USER 10001:10001

# see exceptions: <https://www.shellcheck.net/wiki/SC2016>
# hadolint ignore=SC2016
RUN <<EOF
echo 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc
echo '[[ -s "/usr/local/sdkman/bin/sdkman-init.sh" ]] && . "/usr/local/sdkman/bin/sdkman-init.sh"' >> ~/.bashrc
. "/usr/local/sdkman/bin/sdkman-init.sh"
java --version
EOF

USER 0
RUN cp /home/coder/.bashrc /etc/skel/

USER 10001:10001
