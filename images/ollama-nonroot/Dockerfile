FROM docker.io/ollama/ollama:0.11.5@sha256:802596626817a4f24ae26c7e3e3e0ba368cfb93e3945fc176bb714000abcbb4d

RUN groupadd -r -g 65532 ollama && useradd --create-home --shell /bin/bash --uid 65532 -g ollama ollama

USER 65532:65532
