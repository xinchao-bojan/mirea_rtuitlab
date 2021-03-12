FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get -y install cron


RUN mkdir -p /usr/src/factory/
WORKDIR /usr/src/factory
COPY requirements.txt /usr/src/factory/
RUN pip install -r requirements.txt
COPY . /usr/src/factory/



