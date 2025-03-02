ARG DSF_VERSION=1.7.0
ARG DSF_PROCESS_PING_PONG=1.0.1.0
ARG DSF_PROCESS_ALLOW_LIST=1.0.0.1
ARG DSF_PROCESS_FEASIBILITY=1.0.1.0-alpha.1
ARG DSF_PROCESS_MII_REPORT=1.1.2.0
ARG DSF_PROCESS_MII_DATA_TRANSFER=1.0.3.0
ARG DSF_PROCESS_MII_DATA_SHARING=1.0.2.0
ARG DSF_PROCESS_NCT_DATA_TRANSFER=1.0.0.0-M1

FROM curlimages/curl:8.12.1@sha256:94e9e444bcba979c2ea12e27ae39bee4cd10bc7041a472c4727a558e213744e6 AS deps

ARG DSF_PROCESS_PING_PONG
ARG DSF_PROCESS_ALLOW_LIST
ARG DSF_PROCESS_FEASIBILITY
ARG DSF_PROCESS_MII_REPORT
ARG DSF_PROCESS_MII_DATA_TRANSFER
ARG DSF_PROCESS_MII_DATA_SHARING
ARG DSF_PROCESS_NCT_DATA_TRANSFER

USER root

SHELL ["/bin/ash", "-eo", "pipefail", "-c"]
RUN mkdir -p /process && \
    curl -Lo /process/dsf-process-ping-pong-${DSF_PROCESS_PING_PONG}.jar https://github.com/datasharingframework/dsf-process-ping-pong/releases/download/v${DSF_PROCESS_PING_PONG}/dsf-process-ping-pong-${DSF_PROCESS_PING_PONG}.jar && \
    curl -Lo /process/dsf-process-allow-list-${DSF_PROCESS_ALLOW_LIST}.jar https://github.com/datasharingframework/dsf-process-allow-list/releases/download/v${DSF_PROCESS_ALLOW_LIST}/dsf-process-allow-list-${DSF_PROCESS_ALLOW_LIST}.jar && \
    curl -Lo /process/mii-process-feasibility-${DSF_PROCESS_FEASIBILITY}.jar https://github.com/medizininformatik-initiative/mii-process-feasibility/releases/download/v${DSF_PROCESS_FEASIBILITY}/mii-process-feasibility-${DSF_PROCESS_FEASIBILITY}.jar && \
    curl -Lo /process/mii-process-report-${DSF_PROCESS_MII_REPORT}.jar https://github.com/medizininformatik-initiative/mii-process-report/releases/download/v${DSF_PROCESS_MII_REPORT}/mii-process-report-${DSF_PROCESS_MII_REPORT}.jar && \
    curl -Lo /process/mii-process-data-transfer-${DSF_PROCESS_MII_DATA_TRANSFER}.jar https://github.com/medizininformatik-initiative/mii-process-data-transfer/releases/download/v${DSF_PROCESS_MII_DATA_TRANSFER}/mii-process-data-transfer-${DSF_PROCESS_MII_DATA_TRANSFER}.jar && \
    curl -Lo /process/mii-process-data-sharing-${DSF_PROCESS_MII_DATA_SHARING}.jar https://github.com/medizininformatik-initiative/mii-process-data-sharing/releases/download/v${DSF_PROCESS_MII_DATA_SHARING}/mii-process-data-sharing-${DSF_PROCESS_MII_DATA_SHARING}.jar && \
    chmod 440  /process/*

# this plugin has no public source repository, so far
COPY nct-process-data-transfer-${DSF_PROCESS_NCT_DATA_TRANSFER}.jar /process/
RUN chmod 440  /process/*

USER 1000


FROM ghcr.io/datasharingframework/bpe:1.7.0@sha256:22c05b6ae9aa19a6e27c39e438ace1502c300785f9cf505ed1434a26f7ac48c0

USER root

COPY --from=deps /process/*.jar /opt/bpe/process/

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
ARG DSF_PROCESS_NCT_DATA_TRANSFER

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
    org.miracum.mii.image.dsf-process-nct-data-transfer-version=${DSF_PROCESS_NCT_DATA_TRANSFER} \
    org.opencontainers.image.base.name=ghcr.io/highmed/bpe:${DSF_VERSION} \
    org.opencontainers.image.created=${BUILD_TIME} \
    org.opencontainers.image.authors="info@miracum.de" \
    org.opencontainers.image.source=${SOURCE_REPO} \
    org.opencontainers.image.version=${VERSION} \
    org.opencontainers.image.revision=${IMAGE_REVISION} \
    org.opencontainers.image.vendor="MIRACUM" \
    org.opencontainers.image.title=${IMAGE_TITLE} \
    org.opencontainers.image.description=${IMAGE_DESCRIPTION}
