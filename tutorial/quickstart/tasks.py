import logging

from celery import shared_task

log = logging.getLogger(__name__)

@shared_task
def example_celery_task():
    log.info("This is a log message from a celery task")
