FROM python:3.8-slim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY ./requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./swagger_server/ ./swagger_server/

COPY ./docker_main.py .

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["./docker_main.py"]