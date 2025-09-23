FROM quay.io/strimzi/kafka:0.45.1-kafka-3.9.1@sha256:ba52ed046b1dccdbd96f4e68057ce014d862a7c9c1fc670760c023b9aa09f23f
SHELL ["/bin/bash", "-eo", "pipefail", "-c"]

ARG CONFLUENT_CONNECT_TRANSFORMS_VERSION=1.6.2
ARG CONFLUENT_KAFKA_CONNECT_JDBC_PLUGIN_VERSION=10.8.4

# renovate: datasource=maven depName=com.oracle.database.jdbc:ojdbc11
ARG ORACLE_OJDBC_VERSION=23.9.0.25.07
# renovate: datasource=maven depName=com.microsoft.sqlserver:mssql-jdbc
ARG MSSQL_JDBC_VERSION=13.2.0.jre11
# renovate: datasource=maven depName=org.apache.kafka:connect-file
ARG KAFKA_CONNECT_FILE_VERSION=4.1.0
# renovate: datasource=github-releases depName=Aiven-Open/transforms-for-apache-kafka-connect
ARG AIVEN_TRANSFORMS_FOR_APACHE_KAFKA_CONNECT_VERSION=1.6.0
# renovate: datasource=maven depName=com.github.castorm:kafka-connect-http
ARG CASTORM_KAFKA_CONNECT_HTTP_VERSION=0.8.11
# renovate: datasource=github-releases depName=streamthoughts/kafka-connect-file-pulse
ARG KAFKA_CONNECT_FILE_PULSE_VERSION=2.15.0

USER root

# hadolint ignore=DL3041
RUN <<EOF
microdnf install -y --nodocs unzip
microdnf clean all
EOF

RUN <<EOF
mkdir -p /opt/kafka/plugins/

curl -fLsSO https://hub-downloads.confluent.io/api/plugins/confluentinc/kafka-connect-jdbc/versions/${CONFLUENT_KAFKA_CONNECT_JDBC_PLUGIN_VERSION}/confluentinc-kafka-connect-jdbc-${CONFLUENT_KAFKA_CONNECT_JDBC_PLUGIN_VERSION}.zip
unzip confluentinc-kafka-connect-jdbc-${CONFLUENT_KAFKA_CONNECT_JDBC_PLUGIN_VERSION}.zip -d /opt/kafka/plugins/
rm confluentinc-kafka-connect-jdbc-${CONFLUENT_KAFKA_CONNECT_JDBC_PLUGIN_VERSION}.zip

curl -fLsSO https://hub-downloads.confluent.io/api/plugins/confluentinc/connect-transforms/versions/${CONFLUENT_CONNECT_TRANSFORMS_VERSION}/confluentinc-connect-transforms-${CONFLUENT_CONNECT_TRANSFORMS_VERSION}.zip
unzip confluentinc-connect-transforms-${CONFLUENT_CONNECT_TRANSFORMS_VERSION}.zip -d /opt/kafka/plugins/
rm confluentinc-connect-transforms-${CONFLUENT_CONNECT_TRANSFORMS_VERSION}.zip

curl -fLsSO https://github.com/aiven/transforms-for-apache-kafka-connect/releases/download/v${AIVEN_TRANSFORMS_FOR_APACHE_KAFKA_CONNECT_VERSION}/transforms-for-apache-kafka-connect-${AIVEN_TRANSFORMS_FOR_APACHE_KAFKA_CONNECT_VERSION}.zip
unzip transforms-for-apache-kafka-connect-${AIVEN_TRANSFORMS_FOR_APACHE_KAFKA_CONNECT_VERSION}.zip -d /opt/kafka/plugins/
rm transforms-for-apache-kafka-connect-${AIVEN_TRANSFORMS_FOR_APACHE_KAFKA_CONNECT_VERSION}.zip

curl -fLsSO https://github.com/streamthoughts/kafka-connect-file-pulse/releases/download/v${KAFKA_CONNECT_FILE_PULSE_VERSION}/streamthoughts-kafka-connect-file-pulse-${KAFKA_CONNECT_FILE_PULSE_VERSION}.zip
unzip streamthoughts-kafka-connect-file-pulse-${KAFKA_CONNECT_FILE_PULSE_VERSION}.zip -d /opt/kafka/plugins/
rm streamthoughts-kafka-connect-file-pulse-${KAFKA_CONNECT_FILE_PULSE_VERSION}.zip

curl -fLsSO --output-dir /opt/kafka/libs/ "https://repo1.maven.org/maven2/com/oracle/database/jdbc/ojdbc11/${ORACLE_OJDBC_VERSION}/ojdbc11-${ORACLE_OJDBC_VERSION}.jar"
curl -fLsSO --output-dir /opt/kafka/libs/ "https://repo1.maven.org/maven2/com/microsoft/sqlserver/mssql-jdbc/${MSSQL_JDBC_VERSION}/mssql-jdbc-${MSSQL_JDBC_VERSION}.jar"
curl -fLsSO --output-dir /opt/kafka/libs/ "https://repo1.maven.org/maven2/org/apache/kafka/connect-file/${KAFKA_CONNECT_FILE_VERSION}/connect-file-${KAFKA_CONNECT_FILE_VERSION}.jar"
curl -fLsSO --output-dir /opt/kafka/libs/ "https://repo1.maven.org/maven2/com/github/castorm/kafka-connect-http/${CASTORM_KAFKA_CONNECT_HTTP_VERSION}/kafka-connect-http-${CASTORM_KAFKA_CONNECT_HTTP_VERSION}.jar"
EOF

USER 1001:1001
