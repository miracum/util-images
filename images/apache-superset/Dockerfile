FROM docker.io/apache/superset:6.1.0@sha256:16b50bbef6648912a79e3293d418fefa743ce555d36c5af6b85d859119ed7f88
SHELL ["/bin/bash", "-eo", "pipefail", "-c"]

USER root

# via https://help.ubuntu.com/community/Oracle%20Instant%20Client
# hadolint ignore=DL3008
RUN <<EOF
set -e
apt-get update -y
apt-get install -y --no-install-recommends alien libaio-dev libaio1 unzip wget default-libmysqlclient-dev build-essential pkg-config
rm -rf /var/lib/apt/lists/*
apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false
wget -q https://download.oracle.com/otn_software/linux/instantclient/2360000/oracle-instantclient-basic-23.6.0.24.10-1.el9.x86_64.rpm
alien -i oracle-instantclient-basic-23.6.0.24.10-1.el9.x86_64.rpm
rm oracle-instantclient-basic-23.6.0.24.10-1.el9.x86_64.rpm
EOF

WORKDIR /app
COPY requirements.txt .

# hadolint ignore=SC1091
RUN <<EOF
source /app/.venv/bin/activate
uv pip install --no-cache-dir -r requirements.txt
EOF

USER superset
