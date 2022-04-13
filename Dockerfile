# syntax=docker/dockerfile:1

from python:3.8-alpine3.15

ARG flask_app=gce_metadata_simulator
ARG flask_env=development

ENV FLASK_APP=${flask_app}
ENV FLASK_ENV=${flask_env}

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app/

CMD [ "flask", "run", "--host=0.0.0.0"]
