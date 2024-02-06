FROM docker.io/apache/superset:3.1.0@sha256:9260e32b93fd029550359699fd32cb723567e0cdd09ecc65114f70476d1f0943

USER root

# via <https://github.com/apache/superset/issues/20371#issuecomment-1155750921>
WORKDIR /usr/share/oracle/network/admin

# hadolint ignore=DL3008
RUN apt-get update -y \
    && apt-get install -y --no-install-recommends wget unzip libaio1 libaio-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && wget https://download.oracle.com/otn_software/linux/instantclient/23c/instantclient-basic-linux.x64-23.3.0.0.0.zip \
    && unzip instantclient-basic-linux.x64-23.3.0.0.0.zip \
    && rm -f instantclient-basic-linux.x64-23.3.0.0.0.zip \
    && echo  /usr/share/oracle/instantclient* > /etc/ld.so.conf.d/oracle-instantclient.conf \
    && ldconfig \
    && echo 'local_xe=(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=oracle)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=xepdb1)))' > /usr/share/oracle/network/admin/tnsnames.ora

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

USER superset
