FROM python:3.10-slim

RUN pip install --upgrade pip
WORKDIR /var/docker-python

COPY requirements.txt /var/docker-python
