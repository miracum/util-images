FROM docker.io/ollama/ollama:0.9.2@sha256:5d2f63e9e6ba753c8774991d95cf9091b5c35a0f84e1801a530b4f3fcef0e329

RUN groupadd -r -g 65532 ollama && useradd --create-home --shell /bin/bash --uid 65532 -g ollama ollama

USER 65532:65532
