FROM ghcr.io/omnigent-ai/omnigent-server:v0.22.0@sha256:2e9dacbc28a01d12408ceb5c0f09694cc51d91f53684926a2146a7a47422f417
SHELL ["/bin/bash", "-eo", "pipefail", "-c"]

COPY requirements.txt /tmp/requirements.txt

# adds the dependencies of the upstream `s3`, `tracing`, `kubernetes`, and `openshell` extras, i.e. the equivalent of building the
# upstream image with `--build-arg OMNIGENT_EXTRAS=s3,tracing,kubernetes,openshell`. Required to store artifacts in S3
# (`OMNIGENT_ARTIFACT_URI=s3://...`), to export metrics and traces via OTLP, and to launch managed sandboxes
# (`sandbox.provider: kubernetes`, `agent_sandbox`, or `openshell`).
RUN <<EOF
pip install --no-cache-dir -r /tmp/requirements.txt
rm /tmp/requirements.txt
chown -R 65532:65532 /data
EOF

# the upstream image runs as root
USER 65532:65532
