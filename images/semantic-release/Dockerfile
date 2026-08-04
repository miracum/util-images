FROM docker.io/library/node:24.18.0@sha256:5711a0d445a1af54af9589066c646df387d1831a608226f4cd694fc59e745059
SHELL ["/bin/bash", "-eo", "pipefail", "-c"]
WORKDIR /app
ENV NO_UPDATE_NOTIFIER=true \
    NODE_ENV=production \
    PATH="$PATH:/app/node_modules/.bin"
ENTRYPOINT ["/bin/bash"]

# hadolint ignore=DL3008
RUN <<EOF
apt-get update
apt-get install --no-install-recommends -y git bash
apt-get clean
rm -rf /var/lib/apt/lists/*
EOF

COPY . .

RUN npm clean-install

USER 1000:1000
