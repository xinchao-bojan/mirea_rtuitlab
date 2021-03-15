FROM python:3.9.0b4-alpine3.12


#COPY root /var/spool/cron/crontabs/root

RUN mkdir -p /usr/src/factory/
WORKDIR /usr/src/factory
COPY . .
RUN pip install -r requirements.txt

#
#RUN chmod +x /usr/src/factory/main_app/pycron.py
#CMD crond -l 2 -f
RUN python manage.py crontab add
RUN python manage.py crontab show


