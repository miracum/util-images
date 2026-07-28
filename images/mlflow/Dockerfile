FROM ghcr.io/mlflow/mlflow:v3.14.0-full@sha256:73365f742d67ef9e59e50118010bf14ff825a157c8244051baea887b8587e772
SHELL ["/bin/bash", "-eo", "pipefail", "-c"]

COPY requirements.txt .

# hadolint ignore=SC1091
RUN <<EOF
pip install --no-cache-dir -r requirements.txt
EOF

