from celery import shared_task
import time

@shared_task
def sample_task():
    print("The sample task just ran.")
