FROM ghcr.io/miracum/util-images/spark-delta:v1.7.2@sha256:65ad3cb0203d665be49ff70fceb6e6d2113fb58965e2200e06f48dd7800604f2
WORKDIR /opt/warehousekeeper

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY warehousekeeper.py .

ENV IS_RUNNING_IN_CONTAINER="true"
USER 185:185
ENTRYPOINT [ "python3", "/opt/warehousekeeper/warehousekeeper.py" ]
CMD [ "--help" ]
