FROM docker.io/ollama/ollama:0.5.11@sha256:82956f40bb1f307c77f7a8c3ed91c7a37e072ed757ff143e34210a7b991b9480

RUN groupadd -r -g 65532 ollama && useradd --create-home --shell /bin/bash --uid 65532 -g ollama ollama

USER 65532:65532
