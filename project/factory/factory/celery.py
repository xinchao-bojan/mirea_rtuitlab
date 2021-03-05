from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab


from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'factory.settings')
app = Celery('factory')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'delivery': {
        'task': 'main_app.tasks.delivery',
        'schedule': crontab(minute='*/1'),
        'args': ()
    }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')