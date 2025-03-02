FROM docker.io/ollama/ollama:0.5.12@sha256:251f814864b3ed17ea8740b89a00363c5f14a3ca3738644fdec622eea78d3305

RUN groupadd -r -g 65532 ollama && useradd --create-home --shell /bin/bash --uid 65532 -g ollama ollama

USER 65532:65532
