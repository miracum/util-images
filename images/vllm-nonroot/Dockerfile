FROM docker.io/vllm/vllm-openai:v0.9.2@sha256:37cd5bd18d220a0f4c70401ce1d4a0cc588fbfe03cc210579428f2c47e6eac33

RUN groupadd -r -g 65532 vllm && \
    useradd --create-home --shell /bin/bash --uid 65532 -g vllm vllm

USER 65532:65532
