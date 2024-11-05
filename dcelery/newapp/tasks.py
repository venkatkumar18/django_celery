from celery import shared_task
import time

@shared_task
def task1(queue='celery'):
    time.sleep(3)
    return "\nWelcomce to task1\n\n"

@shared_task
def task2(queue='celery:1'):
    time.sleep(3)
    return "\nWelcome to task2\n\n"

@shared_task
def task3(queue='celery:2'):
    time.sleep(3)
    return "\nWelcomce to task3\n\n"

@shared_task
def task4(queue='celery:3'):
    time.sleep(3)
    return "\nWelcome to task4\n\n"