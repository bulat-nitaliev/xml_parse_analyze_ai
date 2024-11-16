import os, time
from celery import Celery
from django.conf import settings
from celery.schedules import crontab



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'analyzer_service.settings')

app = Celery('core')
app.config_from_object('django.conf:settings')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send-spam': {
        'task' : 'core.tasks.debug_task',
        'schedule': crontab(minute=0, hour=9),
    },
   
}

