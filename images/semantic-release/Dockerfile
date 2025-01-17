FROM docker.io/library/node:22.13.0@sha256:fa54405993eaa6bab6b6e460f5f3e945a2e2f07942ba31c0e297a7d9c2041f62
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
