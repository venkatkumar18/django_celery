from dcelery.celery_config import app
from time import sleep
import sys

@app.task(queue='tasks', time_limit=10)
def long_running_task():
    sleep(6)
    return "Task Completed"

def execute_task():
    task1 = long_running_task.delay()
    try:
        result = task1.get(timeout=4)
    except TimeoutError:
        print(f'Inside TimeoutError - {task1.status}')
        task1.revoke(terminate=True)
        sleep(3)
        print(f'Inside TimeoutError - {task1.status}')
        sys.stdout.write(task1.status)
    print(result)