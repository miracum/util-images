FROM docker.io/ollama/ollama:0.6.4@sha256:476b956cbe76f22494f08400757ba302fd8ab6573965c09f1e1a66b2a7b0eb77

RUN groupadd -r -g 65532 ollama && useradd --create-home --shell /bin/bash --uid 65532 -g ollama ollama

USER 65532:65532
