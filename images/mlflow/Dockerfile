FROM ghcr.io/mlflow/mlflow:v3.17.1-full@sha256:190306b1739b9646d6d39333594334b69ba14ab843db927712c790b50892f262
SHELL ["/bin/bash", "-eo", "pipefail", "-c"]
WORKDIR /

COPY requirements.txt .

# hadolint ignore=SC1091
RUN <<EOF
pip install --no-cache-dir -r requirements.txt
EOF

USER 65534:65534
