FROM docker.io/ollama/ollama:0.10.0@sha256:0f32507862099ab43018cfd782f2586d6c2e561b0c953f2a7ff096f72ea9f2e5

RUN groupadd -r -g 65532 ollama && useradd --create-home --shell /bin/bash --uid 65532 -g ollama ollama

USER 65532:65532
