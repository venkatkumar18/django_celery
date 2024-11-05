from celery import shared_task

@shared_task
def task1():
    return "Welcomce to task1"

@shared_task
def task2():
    return "Welcome to task2"