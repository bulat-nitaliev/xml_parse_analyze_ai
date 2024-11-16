import time
from celery import shared_task
from django.conf import settings



        



@shared_task()
def debug_task():
    time.sleep(20)
    print('Hello debug_task')