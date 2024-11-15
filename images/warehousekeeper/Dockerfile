FROM ghcr.io/miracum/util-images/spark-delta:v1.7.4@sha256:f2e5c4076a79dfccfe9163b13a14952ab826fc777b5c4a66aa077d65c7d0609d
WORKDIR /opt/warehousekeeper

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY warehousekeeper.py .

ENV IS_RUNNING_IN_CONTAINER="true"
USER 185:185
ENTRYPOINT [ "python3", "/opt/warehousekeeper/warehousekeeper.py" ]
CMD [ "--help" ]
