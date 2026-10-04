FROM ghcr.io/mlflow/mlflow:v3.16.1-full@sha256:6af326440af64565c2ea5d1d28c9ee355f70a8d4af5b76e35938365e1ce2e428
SHELL ["/bin/bash", "-eo", "pipefail", "-c"]
WORKDIR /

COPY requirements.txt .

# hadolint ignore=SC1091
RUN <<EOF
pip install --no-cache-dir -r requirements.txt
EOF

USER 65534:65534
