FROM ghcr.io/mlflow/mlflow:v3.15.1-full@sha256:9f9276e57cda1593cfa0fe8519145cd49328e119e85951851b9244e82e3769be
SHELL ["/bin/bash", "-eo", "pipefail", "-c"]
WORKDIR /

COPY requirements.txt .

# hadolint ignore=SC1091
RUN <<EOF
pip install --no-cache-dir -r requirements.txt
EOF

USER 65534:65534
