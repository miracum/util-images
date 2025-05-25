FROM docker.io/ollama/ollama:0.7.1@sha256:de659b95818c5ea17dc287a2e4f147f81e202d84f1dc4ad3f256c53fb81e8dd0

RUN groupadd -r -g 65532 ollama && useradd --create-home --shell /bin/bash --uid 65532 -g ollama ollama

USER 65532:65532
