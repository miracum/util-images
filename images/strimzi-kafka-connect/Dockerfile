FROM quay.io/strimzi/kafka:0.45.1-kafka-3.8.0@sha256:173cb5793756f75739c51a83bbe06d7f0094fd003a2982160a5cc6e216cd6d28

ARG CONFLUENT_CONNECT_TRANSFORMS_VERSION=1.4.7
ARG CONFLUENT_KAFKA_CONNECT_JDBC_PLUGIN_VERSION=10.7.4

# renovate: datasource=maven depName=com.oracle.database.jdbc:ojdbc11
ARG ORACLE_OJDBC_VERSION=23.8.0.25.04
# renovate: datasource=maven depName=com.microsoft.sqlserver:mssql-jdbc
ARG MSSQL_JDBC_VERSION=12.6.0
# renovate: datasource=maven depName=org.apache.kafka:connect-file
ARG KAFKA_CONNECT_FILE_VERSION=3.5.2
# renovate: datasource=github-releases depName=Aiven-Open/transforms-for-apache-kafka-connect
ARG AIVEN_TRANSFORMS_FOR_APACHE_KAFKA_CONNECT_VERSION=1.6.0
# renovate: datasource=maven depName=com.github.castorm:kafka-connect-http
ARG CASTORM_KAFKA_CONNECT_HTTP_VERSION=0.8.11

USER root

# hadolint ignore=DL3041
RUN <<EOF
microdnf install -y --nodocs unzip
microdnf clean all
EOF

RUN <<EOF
mkdir -p /opt/kafka/plugins/

curl -LsSO https://d1i4a15mxbxib1.cloudfront.net/api/plugins/confluentinc/kafka-connect-jdbc/versions/${CONFLUENT_KAFKA_CONNECT_JDBC_PLUGIN_VERSION}/confluentinc-kafka-connect-jdbc-${CONFLUENT_KAFKA_CONNECT_JDBC_PLUGIN_VERSION}.zip
unzip confluentinc-kafka-connect-jdbc-${CONFLUENT_KAFKA_CONNECT_JDBC_PLUGIN_VERSION}.zip -d /opt/kafka/plugins/
rm confluentinc-kafka-connect-jdbc-${CONFLUENT_KAFKA_CONNECT_JDBC_PLUGIN_VERSION}.zip

curl -LsSO https://d1i4a15mxbxib1.cloudfront.net/api/plugins/confluentinc/connect-transforms/versions/${CONFLUENT_CONNECT_TRANSFORMS_VERSION}/confluentinc-connect-transforms-${CONFLUENT_CONNECT_TRANSFORMS_VERSION}.zip
unzip confluentinc-connect-transforms-${CONFLUENT_CONNECT_TRANSFORMS_VERSION}.zip -d /opt/kafka/plugins/
rm confluentinc-connect-transforms-${CONFLUENT_CONNECT_TRANSFORMS_VERSION}.zip

curl -LsSO https://github.com/aiven/transforms-for-apache-kafka-connect/releases/download/v${AIVEN_TRANSFORMS_FOR_APACHE_KAFKA_CONNECT_VERSION}/transforms-for-apache-kafka-connect-${AIVEN_TRANSFORMS_FOR_APACHE_KAFKA_CONNECT_VERSION}.zip
unzip transforms-for-apache-kafka-connect-${AIVEN_TRANSFORMS_FOR_APACHE_KAFKA_CONNECT_VERSION}.zip -d /opt/kafka/plugins/
rm transforms-for-apache-kafka-connect-${AIVEN_TRANSFORMS_FOR_APACHE_KAFKA_CONNECT_VERSION}.zip

curl -LsSO https://repo1.maven.org/maven2/com/github/castorm/kafka-connect-http/${CASTORM_KAFKA_CONNECT_HTTP_VERSION}/kafka-connect-http-${CASTORM_KAFKA_CONNECT_HTTP_VERSION}.zip
unzip kafka-connect-http-${CASTORM_KAFKA_CONNECT_HTTP_VERSION}.zip -d /opt/kafka/plugins/
rm kafka-connect-http-${CASTORM_KAFKA_CONNECT_HTTP_VERSION}.zip
EOF

RUN <<EOF
curl -LsS "https://repo1.maven.org/maven2/com/oracle/database/jdbc/ojdbc11/${ORACLE_OJDBC_VERSION}/ojdbc11-${ORACLE_OJDBC_VERSION}.jar" > "/opt/kafka/libs/ojdbc11-${ORACLE_OJDBC_VERSION}.jar"

curl -LsS "https://repo1.maven.org/maven2/com/microsoft/sqlserver/mssql-jdbc/${MSSQL_JDBC_VERSION}.jre11/mssql-jdbc-${MSSQL_JDBC_VERSION}.jre11.jar" > "/opt/kafka/libs/mssql-jdbc-${MSSQL_JDBC_VERSION}.jre11.jar"

curl -LsS "https://repo1.maven.org/maven2/org/apache/kafka/connect-file/${KAFKA_CONNECT_FILE_VERSION}/connect-file-${KAFKA_CONNECT_FILE_VERSION}.jar" > "/opt/kafka/plugins/connect-file-${KAFKA_CONNECT_VERSION}.jar"
EOF

USER 1001:1001
