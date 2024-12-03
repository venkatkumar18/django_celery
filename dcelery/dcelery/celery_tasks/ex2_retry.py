from dcelery.celery_config import app
from celery import Task
import logging
logging.basicConfig(filename='app.log', level=logging.ERROR, format='%(asctime)s %(levelname)s %(message)s')

class CustomTask(Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        if isinstance(exc, ConnectionError):
            logging.error('Connection Error occurred - Admin Notified')
        else:
            logging.error(f"{task_id} Failure - {exc}")
        # return super().on_failure(exc, task_id, args, kwargs, einfo)

app.Task = CustomTask

@app.task(queue='tasks', autoretry_for=(ConnectionError,), default_retry_delay=5, retry_kwargs={'max_retries': 5})
def tasK_retry():
    raise ConnectionError()