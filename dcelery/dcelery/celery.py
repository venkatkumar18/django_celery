import os
from celery import Celery
from kombu import Exchange, Queue
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcelery.settings')

app = Celery('dcelery')
app.config_from_object("django.conf:settings", namespace="CELERY")

## RabbitMq configuration

app.conf.task_queues = [
    Queue('tasks', Exchange('tasks'), routing_key='tasks',
          queue_arguments={'x-max-priority': 10}),
]

app.conf.task_acks_late = True       # No need to acknowledge immediately after receving the task
app.conf.task_default_priority = 5   # Set a default priority to all the task
app.conf.worker_prefetch_multiplier = 1 # Celery fetches task from queue, it tell how many to fetch it
app.conf.worker_concurrency = 1         # How many task to execute concurrently

@app.task(queue='tasks')
def t1(a,b,**kwargs):
    time.sleep(3)
    result = a * b
    message = kwargs.get('message')
    if message:
        result = f"{message}: {result}"
    return result

@app.task(queue='tasks')
def t2():
    time.sleep(3)
    return "Welcome to T2"

@app.task(queue='tasks')
def t3():
    time.sleep(3)
    return "Welcome to T3"


## Redis Configuration
# app.conf.task_default_rate_limit = '2/m'
# # app.conf.task_routes = {"newapp.tasks.task1": {"queue": "queue1"}, "newapp.tasks.task2": {"queue": "queue2"}}

# app.conf.broker_transport_option = {
#     "priority+steps": list(range(10)),
#     'sep': ':',
#     "queue_order_strategy": 'priority'
# }

app.autodiscover_tasks()


def test():
    kwargs = {"message": "Multiplication of two numbers is"}
    result = t1.apply_async(args=[50,80],kwargs=kwargs,priority=9)
    
    if result.ready():
        print('Task is completed')
    else:
        print('Task is still running')
    
    if result.successful():
        print('Task is completed')
    else:
        print('Task may be still running or a exception may have occurred')

    try:
        return_value = result.get()
        print(f'Return value = {return_value}')
    except Exception as e:
        print(f'Exception occurred during get result - {e}')