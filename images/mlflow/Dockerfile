FROM ghcr.io/mlflow/mlflow:v3.16.0-full@sha256:e72e134e4fd38a229cfbce1b8a8c19c6b4e8928f1ceb5dc136c891855212e998
SHELL ["/bin/bash", "-eo", "pipefail", "-c"]
WORKDIR /

COPY requirements.txt .

# hadolint ignore=SC1091
RUN <<EOF
pip install --no-cache-dir -r requirements.txt
EOF

USER 65534:65534
