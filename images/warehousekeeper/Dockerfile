FROM ghcr.io/miracum/util-images/spark-delta:v1.7.3@sha256:95f96c053ee84976d7047a4639b10c9dc43476dbcec067b7849f3a28fbd4ed2c
WORKDIR /opt/warehousekeeper

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY warehousekeeper.py .

ENV IS_RUNNING_IN_CONTAINER="true"
USER 185:185
ENTRYPOINT [ "python3", "/opt/warehousekeeper/warehousekeeper.py" ]
CMD [ "--help" ]
