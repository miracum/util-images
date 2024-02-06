FROM docker.io/apache/superset:3.1.0@sha256:9260e32b93fd029550359699fd32cb723567e0cdd09ecc65114f70476d1f0943
WORKDIR /app

USER root

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

USER superset
