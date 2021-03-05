from __future__ import absolute_import, unicode_literals


from celery import shared_task
from main_app.views import delivering


@shared_task
def delivery():
    delivering()
