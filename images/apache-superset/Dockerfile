FROM docker.io/apache/superset:3.1.0@sha256:63c4a6948a7ba49bc6a4d321e81fdec7e13d7d2b36b432efba738c1a4317238f

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
