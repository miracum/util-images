# syntax=docker/dockerfile:1.7.0@sha256:dbbd5e059e8a07ff7ea6233b213b36aa516b4c53c645f1817a4dd18b83cbea56
FROM docker.io/codercom/enterprise-base:ubuntu@sha256:b64e9c856c022eddbeb4afe12c9febf882ce5952f7df8465e4a6eed6864d4fda
SHELL ["/bin/bash", "-eo", "pipefail", "-c"]

USER root

# hadolint ignore=DL3008
RUN <<EOF
add-apt-repository ppa:deadsnakes/ppa -y
apt-get update -y
apt-get install -y --no-install-recommends zip unzip git curl python3.12
apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false
apt-get clean
rm -rf /var/lib/apt/lists/*
EOF

USER 1000:1000

# hadolint ignore=SC1091
RUN <<EOF
curl -s "https://get.sdkman.io" | bash
# shellcheck source=/dev/null
source "/home/coder/.sdkman/bin/sdkman-init.sh"
sdk install java 17.0.10-tem
EOF
