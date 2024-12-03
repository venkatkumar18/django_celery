from dcelery.celery_config import app
from celery import group

@app.task(queue='tasks')
def is_even(number):
    if number % 2!=0:
        raise ValueError(f"This number is {number} not an even number")
    else:
        return f"This number is {number} an even number"
    

def handle_result(result):
    if result.successful():
        print(f"SUCCESS: RESULT - {result.get()}")
    elif result.failed():
        print(f"FAILED: RESULT - {result.result}")
    elif result.revoked():
        print(f"REVOKED: RESULT ID = {result.id}")



def run_task():
    group_tasks = group(
        is_even.s(num) for num in range(10)
    )
    result_group = group_tasks.apply_async()
    result_group.get(disable_sync_subtasks=False, propagate=False)
    for res in result_group:
        handle_result(res)