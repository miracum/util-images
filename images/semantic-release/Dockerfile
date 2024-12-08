FROM docker.io/library/node:22.12.0@sha256:35a5dd72bcac4bce43266408b58a02be6ff0b6098ffa6f5435aeea980a8951d7
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
