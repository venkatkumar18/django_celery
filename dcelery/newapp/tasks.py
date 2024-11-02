from celery import shared_task

@shared_task
def add_number():
    return sum(range(100))