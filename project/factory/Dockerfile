FROM python:3


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y cron

COPY my_cron /etc/cron.d/my_cron
RUN chmod 0644 /etc/cron.d/my_cron
RUN crontab /etc/cron.d/my_cron
RUN touch /var/log/cron.log
CMD cron && tail -f /var/log/cron.log

RUN mkdir -p /usr/src/factory/
WORKDIR /usr/src/factory
COPY . .
RUN pip install -r requirements.txt



