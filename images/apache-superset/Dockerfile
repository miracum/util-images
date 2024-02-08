FROM docker.io/apache/superset:3.1.0@sha256:9260e32b93fd029550359699fd32cb723567e0cdd09ecc65114f70476d1f0943

USER root

# via https://help.ubuntu.com/community/Oracle%20Instant%20Client
# hadolint ignore=DL3008
RUN apt-get update -y \
    && apt-get install -y --no-install-recommends wget unzip alien libaio1 libaio-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && wget https://download.oracle.com/otn_software/linux/instantclient/2113000/oracle-instantclient-basic-21.13.0.0.0-1.el8.x86_64.rpm \
    && alien -i oracle-instantclient-basic-21.13.0.0.0-1.el8.x86_64.rpm \
    && rm oracle-instantclient-basic-21.13.0.0.0-1.el8.x86_64.rpm

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

USER superset