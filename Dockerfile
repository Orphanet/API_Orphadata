### STAGE 1:BUILD ###
FROM python:3.10-slim AS build
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
	build-essential gcc

WORKDIR /usr/app
RUN python -m venv /usr/app/venv
ENV PATH="/usr/app/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install gunicorn

### STAGE 2:RUN ###
FROM python:3.10-slim

RUN groupadd -g 999 python && \
    useradd -r -u 999 -g python python

RUN mkdir /usr/app && chown python:python /usr/app
WORKDIR /usr/app

COPY --chown=python:python --from=build /usr/app/venv ./venv
COPY --chown=python:python . .

USER 999

ENV DATA_ENV remote
ENV FLASK_ENV production
ENV ELASTIC_URL https://localhost:9200/
ENV ELASTIC_USER ${ELASTIC_USER}
ENV ELASTIC_PASS ${ELASTIC_PASS}

ENV PATH="/usr/app/venv/bin:$PATH"
CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "wsgi" ]
EXPOSE 5000
