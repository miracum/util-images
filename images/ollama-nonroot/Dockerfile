FROM docker.io/ollama/ollama:0.10.1@sha256:67642615c0fe816cdedefda19c3a82f85bc99bf54c82af2d0f63df2842d4fb48

RUN groupadd -r -g 65532 ollama && useradd --create-home --shell /bin/bash --uid 65532 -g ollama ollama

USER 65532:65532
