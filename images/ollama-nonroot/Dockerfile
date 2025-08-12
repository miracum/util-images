FROM docker.io/ollama/ollama:0.11.4@sha256:be17b353bf3cfab0b6980530284e64716a57589ed753a82d9a6a2a5fa9a61a31

RUN groupadd -r -g 65532 ollama && useradd --create-home --shell /bin/bash --uid 65532 -g ollama ollama

USER 65532:65532
