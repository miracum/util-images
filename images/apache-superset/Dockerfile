FROM docker.io/apache/superset:4.1.1@sha256:1d1fdaaeb19ce9cdba71620ee1cc6117d73813b2f3b422ce5a1bf752c247b7c0

USER root

# via https://help.ubuntu.com/community/Oracle%20Instant%20Client
# hadolint ignore=DL3008
RUN <<EOF
set -e
apt-get update -y
apt-get install -y --no-install-recommends alien libaio-dev libaio1 unzip wget
rm -rf /var/lib/apt/lists/*
apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false
wget -q https://download.oracle.com/otn_software/linux/instantclient/2360000/oracle-instantclient-basic-23.6.0.24.10-1.el9.x86_64.rpm
alien -i oracle-instantclient-basic-23.6.0.24.10-1.el9.x86_64.rpm
rm oracle-instantclient-basic-23.6.0.24.10-1.el9.x86_64.rpm
EOF

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

USER superset
