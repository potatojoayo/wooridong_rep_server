from __future__ import absolute_import, unicode_literals
import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PROJECT_DIR.settings')

app = Celery('PROJECT_DIR')
app.config_from_object('django.conf:settings', namespace='CELERY_TASK')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Require: {0!r}'.format(self.request))