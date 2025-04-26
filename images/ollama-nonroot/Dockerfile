FROM docker.io/ollama/ollama:0.6.6@sha256:d42df3fe2285ca1f9f3b6f90dce394d73d7dd024a63104f9a5056ce1da4db1be

RUN groupadd -r -g 65532 ollama && useradd --create-home --shell /bin/bash --uid 65532 -g ollama ollama

USER 65532:65532
