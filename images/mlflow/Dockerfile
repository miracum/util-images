FROM ghcr.io/mlflow/mlflow:v3.18.0-full@sha256:a8459ca08b1e8a0dc287b4e226d4f2338f56052d7e2d333a4aa5891be0670919
SHELL ["/bin/bash", "-eo", "pipefail", "-c"]
WORKDIR /

COPY requirements.txt .

# hadolint ignore=SC1091
RUN <<EOF
pip install --no-cache-dir -r requirements.txt
EOF

USER 65534:65534
