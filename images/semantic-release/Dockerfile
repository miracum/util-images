FROM docker.io/library/node:20.17.0-slim@sha256:9fb20391a0320aed25636d8312f4332f9be734c5acef4c94722048c2bed5a87d
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
