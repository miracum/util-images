FROM docker.io/apache/superset:2.1.3@sha256:d175fbf9fd0285a6e47c43d0b09abe7ff98644e39f3334d6bab98b761fc2ff91
WORKDIR /app

USER root

COPY requirements.txt .

RUN pip install --require-hashes --no-cache-dir -r requirements.txt

USER superset
