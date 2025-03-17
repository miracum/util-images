FROM docker.io/ollama/ollama:0.6.1@sha256:5592e1b526d0081b9768c6122338d2cf79c4192f0aa34909dd2f97398295ca9d

RUN groupadd -r -g 65532 ollama && useradd --create-home --shell /bin/bash --uid 65532 -g ollama ollama

USER 65532:65532
