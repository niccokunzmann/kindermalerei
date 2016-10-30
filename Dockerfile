# see https://hub.docker.com/_/python/
FROM python:3-alpine

COPY kindermalerei .

EXPOSE 8080

VOLUME /var/kindermalerei

WORKDIR kindermalerei

RUN pip install --no-cache -r requirements.txt

CMD ["python3", "-m", "kindermalerei"]

