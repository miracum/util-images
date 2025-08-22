FROM docker.io/ollama/ollama:0.11.6@sha256:1868fd51253099b8f48b89b981e5d8ba23e4db161a501b86e29593071c1c069b

RUN groupadd -r -g 65532 ollama && useradd --create-home --shell /bin/bash --uid 65532 -g ollama ollama

USER 65532:65532
