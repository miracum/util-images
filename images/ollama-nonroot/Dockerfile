FROM docker.io/ollama/ollama:0.9.6@sha256:f478761c18fea69b1624e095bce0f8aab06825d09ccabcd0f88828db0df185ce

RUN groupadd -r -g 65532 ollama && useradd --create-home --shell /bin/bash --uid 65532 -g ollama ollama

USER 65532:65532
