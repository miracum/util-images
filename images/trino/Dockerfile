FROM docker.io/trinodb/trino:459@sha256:77c7c42ee0e2b4ba6673fb3fbbcd6912ce9bf12a976245759e07f7874b571cb7 AS downloader

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

FROM docker.io/trinodb/trino:459@sha256:77c7c42ee0e2b4ba6673fb3fbbcd6912ce9bf12a976245759e07f7874b571cb7
COPY --from=downloader /usr/lib/trino/plugin/trino-storage-*/ /usr/lib/trino/plugin/storage/
USER 1000:1000
