FROM docker.io/ollama/ollama:0.7.0@sha256:f6699242880c38eb356dfd8204b08b7a7ba4da2645bdece55a0871bf6752a585

RUN groupadd -r -g 65532 ollama && useradd --create-home --shell /bin/bash --uid 65532 -g ollama ollama

USER 65532:65532
