FROM docker.io/ollama/ollama:0.6.7@sha256:b8dc25402640713e75314143ebd0181774a96efa2a0da441370342d3e948cf16

RUN groupadd -r -g 65532 ollama && useradd --create-home --shell /bin/bash --uid 65532 -g ollama ollama

USER 65532:65532
