# see https://hub.docker.com/_/python/
FROM python:3.5.0-slim

# Prepare the environment
RUN pip install --no-cache --upgrade pip
RUN mkdir /app
COPY kindermalerei/ /app/

# install the environment
RUN cd /app && \
    pip install --no-cache -r requirements.txt

# Prepare execution
EXPOSE 80
VOLUME /var/kindermalerei
WORKDIR /app/

ENTRYPOINT ["python3", "server.py"]

