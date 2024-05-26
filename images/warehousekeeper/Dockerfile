FROM ghcr.io/miracum/util-images/spark-delta:v1.7.1@sha256:8c79c0be040fa5c8676577c1a5c0a0bbecf1e780e9ba705770eb76dc06acb127
WORKDIR /opt/warehousekeeper

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY warehousekeeper.py .

ENV IS_RUNNING_IN_CONTAINER="true"
USER 185:185
ENTRYPOINT [ "python3", "/opt/warehousekeeper/warehousekeeper.py" ]
CMD [ "--help" ]
