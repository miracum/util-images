FROM docker.io/cricketeerone/apache-kafka-connect:4.0.0-confluent-hub@sha256:15454efc2dcff3e94317837f5fa72c02d10ec3d55faff4946929d1bc23bf4b26
SHELL ["/bin/bash", "-eo", "pipefail", "-c"]

WORKDIR /app/libs/

RUN <<EOF
confluent-hub install --no-prompt \
    --component-dir /app/libs --worker-configs /app/resources/connect-distributed.properties -- \
    confluentinc/kafka-connect-jdbc:10.8.4

confluent-hub install --no-prompt \
    --component-dir /app/libs --worker-configs /app/resources/connect-distributed.properties -- \
    confluentinc/connect-transforms:1.6.2
EOF

WORKDIR /app/libs/confluentinc-kafka-connect-jdbc/lib/

RUN <<EOF
curl -fLsSO https://repo1.maven.org/maven2/com/mysql/mysql-connector-j/9.3.0/mysql-connector-j-9.3.0.jar
curl -fLsSO https://repo1.maven.org/maven2/org/mariadb/jdbc/mariadb-java-client/3.5.4/mariadb-java-client-3.5.4.jar
curl -fLsSO https://repo1.maven.org/maven2/com/oracle/database/jdbc/ojdbc11/23.8.0.25.04/ojdbc11-23.8.0.25.04.jar
curl -fLsSO https://repo1.maven.org/maven2/org/postgresql/postgresql/42.7.7/postgresql-42.7.7.jar
curl -fLsSO https://repo1.maven.org/maven2/io/trino/trino-jdbc/478/trino-jdbc-478.jar
EOF

WORKDIR /
USER 65534:65534
