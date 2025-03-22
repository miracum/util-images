FROM docker.io/library/node:22.14.0@sha256:c7fd844945a76eeaa83cb372e4d289b4a30b478a1c80e16c685b62c54156285b
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
