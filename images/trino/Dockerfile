FROM docker.io/trinodb/trino:455@sha256:cb08dfd4bd58fb4bec5df09457347c6f353f82d91495305e7648b2bf1307de45 AS downloader

# renovate: datasource=github-releases depName=snowlift/trino-storage
ENV TRINO_STORAGE_PLUGIN_VERSION=454

USER 0

# hadolint ignore=DL3041
RUN <<EOF
microdnf install -y --nodocs unzip
microdnf clean all
curl -LsSO https://github.com/snowlift/trino-storage/releases/download/v${TRINO_STORAGE_PLUGIN_VERSION}/trino-storage-${TRINO_STORAGE_PLUGIN_VERSION}.zip
unzip trino-storage-${TRINO_STORAGE_PLUGIN_VERSION}.zip -d  /usr/lib/trino/plugin/
EOF

USER 1000:1000

FROM docker.io/trinodb/trino:455@sha256:cb08dfd4bd58fb4bec5df09457347c6f353f82d91495305e7648b2bf1307de45
COPY --from=downloader /usr/lib/trino/plugin/trino-storage-*/ /usr/lib/trino/plugin/storage/
USER 1000:1000
