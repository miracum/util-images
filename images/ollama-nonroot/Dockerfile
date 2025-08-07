FROM docker.io/ollama/ollama:0.11.3@sha256:faa2d82a570de80e6f1b70a7e6669c296f315db558b1a593b79a11162f8ba009

RUN groupadd -r -g 65532 ollama && useradd --create-home --shell /bin/bash --uid 65532 -g ollama ollama

USER 65532:65532
