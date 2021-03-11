from celery import shared_task
from django.core.management import call_command


@shared_task
def maradmin_task():
    print("Running Scraper!!!")
    call_command('maradmin_crawl')