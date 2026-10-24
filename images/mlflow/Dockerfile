FROM ghcr.io/mlflow/mlflow:v3.17.2-full@sha256:f922dce73c12026ce7e6b8e3e0740a657db3162910d4368f67dddc86af8b3d10
SHELL ["/bin/bash", "-eo", "pipefail", "-c"]
WORKDIR /

COPY requirements.txt .

# hadolint ignore=SC1091
RUN <<EOF
pip install --no-cache-dir -r requirements.txt
EOF

USER 65534:65534
