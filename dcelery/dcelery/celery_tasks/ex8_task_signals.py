from celery.signals import task_failure
from dcelery.celery_config import app
import sys

@app.task(queue='tasks')
def task_to_be_failed():
    raise ValueError("Task Failed")

@app.task(queue='tasks')
def cleanup_failed_task(task_id,*args,**kwargs):
    sys.stdout.write('<<<<    CLEANUP TASK ...    >>>>')
    sys.stdout.write('<<<<    CLEANUP TASK ...    >>>>')
    return "Completed Cleanup"

@task_failure.connect(sender=task_to_be_failed)
def handle_task_failure(sender=None,task_id=None,**kwargs):
    cleanup_failed_task.delay(task_id)

def run_task():
    task_to_be_failed.apply_async()