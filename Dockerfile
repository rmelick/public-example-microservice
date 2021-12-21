# syntax=docker/dockerfile:1
# This file was taken most from https://hub.docker.com/_/python?tab=description
# with a little bit from https://docs.docker.com/samples/django/
FROM python:3.9.9

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY tutorial .

# we do not set a CMD or Entrypoint, because we want different versions of that for normal django
# web app vs. celery
