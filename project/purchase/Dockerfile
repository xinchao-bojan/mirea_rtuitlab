FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

RUN mkdir -p /usr/src/purchase/
WORKDIR /usr/src/purchase
COPY requirements.txt /usr/src/purchase/
RUN pip install -r requirements.txt
COPY . /usr/src/purchase/

