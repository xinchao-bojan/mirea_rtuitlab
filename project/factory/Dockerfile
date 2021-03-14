FROM python:3.9.0b4-alpine3.12

COPY pycron /bin/pycron
COPY root /var/spool/cron/crontabs/root
RUN chmod +x /bin/pycron
CMD crond -l 2 -f

RUN mkdir -p /usr/src/factory/
WORKDIR /usr/src/factory
COPY . .
RUN pip install -r requirements.txt




