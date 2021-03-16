#FROM python:3.9.0b4-alpine3.12
FROM python:3

RUN mkdir -p /usr/src/factory/
WORKDIR /usr/src/factory
COPY . .

RUN pip install -r requirements.txt

