FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

RUN mkdir -p /usr/src/shop/
WORKDIR /usr/src/shop
COPY requirements.txt /usr/src/shop/
RUN pip install -r requirements.txt
COPY . /usr/src/shop/

