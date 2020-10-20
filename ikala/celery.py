import os
from celery import Celery


# set the default Djanog settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ikala.settings')

app = Celery('ikala')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()