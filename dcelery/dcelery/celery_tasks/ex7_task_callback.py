from dcelery.celery_config import app


@app.task(queue='tasks')
def is_even(num):
    if num % 2 !=0:
        raise ValueError(f"{num} is not an even number")
    return True

@app.task(queue='tasks')
def success_execution1(res):
    print(f'Task executed successfully - 1')
    
@app.task(queue='tasks')
def success_execution2(res):
    print(f'Task executed successfully- 2')

@app.task(queue='tasks')
def failure_execution(task_id,exc,traceback):
    print(f'Task execution failed')

def run_task():
    task1 = is_even.apply_async(args=[4], link=[success_execution1.s(),success_execution2.s(),],link_error=[failure_execution.s(),])
    task2 = is_even.apply_async(args=[6], link=[success_execution1.s(),success_execution2.s(),],link_error=[failure_execution.s(),])
    task3 = is_even.apply_async(args=[3], link=[success_execution1.s(),success_execution2.s(),],link_error=[failure_execution.s(),])
    task4 = is_even.apply_async(args=[1], link=[success_execution1.s(),success_execution2.s(),],link_error=[failure_execution.s(),])
    