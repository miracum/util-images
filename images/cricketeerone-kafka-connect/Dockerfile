FROM docker.io/cricketeerone/apache-kafka-connect:3.5.1-confluent-hub@sha256:73984d7c18f2f2d97f33edc157aac5ccb2c3b66027b1d807b78baeea862472fe

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

EOF

WORKDIR /
USER 65532:65532
