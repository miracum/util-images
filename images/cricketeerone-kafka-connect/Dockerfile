FROM docker.io/cricketeerone/apache-kafka-connect:3.8.0-confluent-hub@sha256:32af2413f749c4b420fc9505f58bc50b90b1780fad5019e90a1cea7d59eb39cb
ENV ORACLE_OJDBC_VERSION=21.11.0.0

WORKDIR /tmp

RUN <<EOF
confluent-hub install --no-prompt \
    --component-dir /app/libs --worker-configs /app/resources/connect-distributed.properties -- \
    confluentinc/kafka-connect-jdbc:10.7.2

confluent-hub install --no-prompt \
    --component-dir /app/libs --worker-configs /app/resources/connect-distributed.properties -- \
    confluentinc/connect-transforms:1.4.3

curl -o /app/libs/confluentinc-kafka-connect-jdbc/lib/mysql-connector-j-8.0.33.jar \
    https://repo1.maven.org/maven2/com/mysql/mysql-connector-j/8.0.33/mysql-connector-j-8.0.33.jar

curl -o /app/libs/confluentinc-kafka-connect-jdbc/lib/mariadb-java-client-3.1.4.jar \
    https://repo1.maven.org/maven2/org/mariadb/jdbc/mariadb-java-client/3.1.4/mariadb-java-client-3.1.4.jar

curl -o /app/libs/confluentinc-kafka-connect-jdbc/lib/ojdbc11-${ORACLE_OJDBC_VERSION}.jar \
    https://repo1.maven.org/maven2/com/oracle/database/jdbc/ojdbc11/${ORACLE_OJDBC_VERSION}/ojdbc11-${ORACLE_OJDBC_VERSION}.jar
EOF

WORKDIR /
USER 65532:65532
