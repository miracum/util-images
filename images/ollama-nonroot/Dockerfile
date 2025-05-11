FROM docker.io/ollama/ollama:0.6.8@sha256:50ab2378567a62b811a2967759dd91f254864c3495cbe50576bd8a85bc6edd56

RUN groupadd -r -g 65532 ollama && useradd --create-home --shell /bin/bash --uid 65532 -g ollama ollama

USER 65532:65532
