FROM docker.io/apache/superset:4.0.2@sha256:51a90d11a59ac522172642cece4bd8047917253e13d884293fcd0cd48419939c

USER root

# via https://help.ubuntu.com/community/Oracle%20Instant%20Client
# hadolint ignore=DL3008
RUN apt-get update -y \
    && apt-get install -y --no-install-recommends wget unzip alien libaio1 libaio-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && wget -q https://download.oracle.com/otn_software/linux/instantclient/2113000/oracle-instantclient-basic-21.13.0.0.0-1.el8.x86_64.rpm \
    && alien -i oracle-instantclient-basic-21.13.0.0.0-1.el8.x86_64.rpm \
    && rm oracle-instantclient-basic-21.13.0.0.0-1.el8.x86_64.rpm

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

USER superset
