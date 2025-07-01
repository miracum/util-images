FROM docker.io/ollama/ollama:0.9.4@sha256:8778ab50911bf22dd398c9ab733fd16ab2ac86b333cba21f0def72e61aa2baf7

RUN groupadd -r -g 65532 ollama && useradd --create-home --shell /bin/bash --uid 65532 -g ollama ollama

USER 65532:65532
