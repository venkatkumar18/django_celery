from dcelery.celery_config import app
from celery import chain

@app.task(queue='tasks')
def add(x,y):
    return x+y

@app.task(queue='tasks')
def multiply(res):
    return res * 2

@app.task(queue='tasks')
def division(res):
    if res == 0:
        raise ValueError("Zero Division Error")
    return res / 2


def run_task():
    chain_tasks1 = chain(add.s(5,6), division.s(), multiply.s())  # The result of add is passed as a parameter to division and the result of division is passed as an parameter to multiply
    chain_tasks2 = chain(add.s(-1,1),division.s(),multiply.s())  # If any one fails it will stop there, will not execute the next
    print(chain_tasks1.apply_async().get())
    print(chain_tasks2.apply_async().get())