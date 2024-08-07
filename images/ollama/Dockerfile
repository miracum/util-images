FROM docker.io/ollama/ollama:0.3.4@sha256:31b45dbe6f713ee6d05d5f72323463044ea32105df4dd0c3e7fd18207f3783c7

RUN groupadd -r -g 65532 ollama && useradd --create-home --shell /bin/bash --uid 65532 -g ollama ollama

USER 65532:65532
# via <https://github.com/ollama/ollama/issues/957#issuecomment-2072069206>
# not great :/
RUN nohup bash -c "ollama serve &" && sleep 15 && ollama pull llama3.1:70b
