""" Celery is a distributed task queue used for real-time processing of 
    asynchronous actions
"""

from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'villafleurie.settings')
app = Celery('villafleurie')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    """ Print request. For debug purposes only. """
    print(f'Request: {self.request!r}')
