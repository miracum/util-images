FROM docker.io/ollama/ollama:0.10.0@sha256:ba618d67d1421cef18d3d9d88e087abb694cc9bbfb8a22f69f7ab3552f684947

RUN groupadd -r -g 65532 ollama && useradd --create-home --shell /bin/bash --uid 65532 -g ollama ollama

USER 65532:65532
