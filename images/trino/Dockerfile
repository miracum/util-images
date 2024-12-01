FROM docker.io/trinodb/trino:466@sha256:fc1e75a9e252fa65bd7dd28c1fc1ba9ad852e2913fe5694e120544b11eecc6f4 AS downloader

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

FROM docker.io/trinodb/trino:466@sha256:fc1e75a9e252fa65bd7dd28c1fc1ba9ad852e2913fe5694e120544b11eecc6f4
COPY --from=downloader /usr/lib/trino/plugin/trino-storage-*/ /usr/lib/trino/plugin/storage/
USER 1000:1000
