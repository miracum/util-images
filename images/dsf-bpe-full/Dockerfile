ARG CA_TAR_URL=https://dsf.dev/download/dsf_bpe_1_6_0.tar.gz
ARG DSF_VERSION=1.6.0
ARG DSF_PROCESS_PING_PONG=1.0.1.0
ARG DSF_PROCESS_ALLOW_LIST=1.0.0.1
ARG DSF_PROCESS_FEASIBILITY=1.0.1.0-alpha.1
ARG DSF_PROCESS_MII_REPORT=1.1.1.1
ARG DSF_PROCESS_MII_DATA_TRANSFER=1.0.2.1
ARG DSF_PROCESS_MII_DATA_SHARING=1.0.1.1

FROM curlimages/curl:8.10.1@sha256:d9b4541e214bcd85196d6e92e2753ac6d0ea699f0af5741f8c6cccbfcf00ef4b AS deps

ARG CA_TAR_URL
ARG DSF_PROCESS_PING_PONG
ARG DSF_PROCESS_ALLOW_LIST
ARG DSF_PROCESS_FEASIBILITY
ARG DSF_PROCESS_MII_REPORT
ARG DSF_PROCESS_MII_DATA_TRANSFER
ARG DSF_PROCESS_MII_DATA_SHARING

USER root

SHELL ["/bin/ash", "-eo", "pipefail", "-c"]
RUN mkdir -p /process /secrets && \
    curl -Lo /process/bpe.tar.gz ${CA_TAR_URL} && \
    tar -xvOz -f /process/bpe.tar.gz bpe/secrets/ssl_root_ca_certificate_file.pem > /secrets/root_ca.pem && \
    tar -xvOz -f /process/bpe.tar.gz bpe/secrets/ssl_ca_certificate_file.pem > /secrets/ca.pem && \
    curl -Lo /process/dsf-process-ping-pong-${DSF_PROCESS_PING_PONG}.jar https://github.com/datasharingframework/dsf-process-ping-pong/releases/download/v${DSF_PROCESS_PING_PONG}/dsf-process-ping-pong-${DSF_PROCESS_PING_PONG}.jar && \
    curl -Lo /process/dsf-process-allow-list-${DSF_PROCESS_ALLOW_LIST}.jar https://github.com/datasharingframework/dsf-process-allow-list/releases/download/v${DSF_PROCESS_ALLOW_LIST}/dsf-process-allow-list-${DSF_PROCESS_ALLOW_LIST}.jar && \
    curl -Lo /process/mii-process-feasibility-${DSF_PROCESS_FEASIBILITY}.jar https://github.com/medizininformatik-initiative/mii-process-feasibility/releases/download/v${DSF_PROCESS_FEASIBILITY}/mii-process-feasibility-${DSF_PROCESS_FEASIBILITY}.jar && \
    curl -Lo /process/mii-process-report-${DSF_PROCESS_MII_REPORT}.jar https://github.com/medizininformatik-initiative/mii-process-report/releases/download/v${DSF_PROCESS_MII_REPORT}/mii-process-report-${DSF_PROCESS_MII_REPORT}.jar && \
    curl -Lo /process/mii-process-data-transfer-${DSF_PROCESS_MII_DATA_TRANSFER}.jar https://github.com/medizininformatik-initiative/mii-process-data-transfer/releases/download/v${DSF_PROCESS_MII_DATA_TRANSFER}/mii-process-data-transfer-${DSF_PROCESS_MII_DATA_TRANSFER}.jar && \
    curl -Lo /process/mii-process-data-sharing-${DSF_PROCESS_MII_DATA_SHARING}.jar https://github.com/medizininformatik-initiative/mii-process-data-sharing/releases/download/v${DSF_PROCESS_MII_DATA_SHARING}/mii-process-data-sharing-${DSF_PROCESS_MII_DATA_SHARING}.jar && \
    chmod 440  /process/*

USER 1000


FROM ghcr.io/datasharingframework/bpe:1.6.0@sha256:7045623daf2283a6a81c5a3a48ff39cb784369a2252c96217b4ed4a404990c16

USER root

COPY --from=deps /process/*.jar /opt/bpe/process/
COPY --from=deps /secrets/* /opt/bpe/secrets/

ENV DEV_DSF_BPE_PROCESS_EXCLUDED="medizininformatik-initiativede_reportReceive|1.1,\
medizininformatik-initiativede_dataReceive|1.0,\
medizininformatik-initiativede_mergeDataSharing|1.0,\
medizininformatik-initiativede_coordinateDataSharing|1.0,\
dsfdev_updateAllowList|1.0"

RUN chown -R 2202:2202 /opt/bpe

USER 2202:2202

ARG DSF_VERSION
ARG DSF_PROCESS_PING_PONG
ARG DSF_PROCESS_ALLOW_LIST
ARG DSF_PROCESS_FEASIBILITY
ARG DSF_PROCESS_MII_REPORT
ARG DSF_PROCESS_MII_DATA_TRANSFER
ARG DSF_PROCESS_MII_DATA_SHARING

ARG BUILD_TIME
ARG IMAGE_DESCRIPTION
ARG IMAGE_REVISION
ARG IMAGE_TITLE
ARG SOURCE_REPO
ARG VERSION
LABEL org.miracum.mii.image.dsf-version=${DSF_VERSION} \
    org.miracum.mii.image.dsf-process-ping-pong-version=${DSF_PROCESS_PING_PONG} \
    org.miracum.mii.image.dsf-process-allow-list-version=${DSF_PROCESS_ALLOW_LIST} \
    org.miracum.mii.image.dsf-process-mii-feasability-version=${DSF_PROCESS_FEASIBILITY} \
    org.miracum.mii.image.dsf-process-mii-report-version=${DSF_PROCESS_MII_REPORT} \
    org.miracum.mii.image.dsf-process-mii-data-transfer-version=${DSF_PROCESS_MII_DATA_TRANSFER} \
    org.miracum.mii.image.dsf-process-mii-data-sharing-version=${DSF_PROCESS_MII_DATA_SHARING} \
    org.opencontainers.image.base.name=ghcr.io/highmed/bpe:${DSF_VERSION} \
    org.opencontainers.image.created=${BUILD_TIME} \
    org.opencontainers.image.authors="info@miracum.de" \
    org.opencontainers.image.source=${SOURCE_REPO} \
    org.opencontainers.image.version=${VERSION} \
    org.opencontainers.image.revision=${IMAGE_REVISION} \
    org.opencontainers.image.vendor="MIRACUM" \
    org.opencontainers.image.title=${IMAGE_TITLE} \
    org.opencontainers.image.description=${IMAGE_DESCRIPTION}
