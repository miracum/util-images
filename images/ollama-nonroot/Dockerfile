FROM docker.io/ollama/ollama:0.5.13@sha256:a79fc15cecf33ed3b05c09a28415db7291c85c4c9d5945f4597317ca02456532

RUN groupadd -r -g 65532 ollama && useradd --create-home --shell /bin/bash --uid 65532 -g ollama ollama

USER 65532:65532
