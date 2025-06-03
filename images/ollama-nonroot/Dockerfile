FROM docker.io/ollama/ollama:0.9.0@sha256:2ea3b768a8f2dcd4d910f838d79702bb952089414dd578146619c0a939647ac6

RUN groupadd -r -g 65532 ollama && useradd --create-home --shell /bin/bash --uid 65532 -g ollama ollama

USER 65532:65532
