from dcelery.celery_config import app
from celery import group
import traceback

app.conf.task_acks_late = True
app.conf.task_reject_on_worker_lost = True


@app.task(queue='tasks')
def is_prime_number(number):
    try:
        is_prime = True
        if number <= 1:
            return False
        for i in range(2,number):
            if number % i==0:
                is_prime =  False
                break
        if not is_prime:
            raise ValueError(f"{number} is not a prime number")
        return is_prime, f"{number} is a prime number"
    except Exception as e:
        traceback_str = traceback.format_exc()
        request_id = is_prime_number.request.id
        handle_task_on_failure.apply_async(args=(number, str(e), request_id, traceback_str))
        raise

@app.task(queue='dead_letter')
def handle_task_on_failure(value, exception, task_id, tracback_result):
    print('Custom logic to process error handling')
    return [value,exception,task_id,tracback_result]

def run_task():
    task_group = group(is_prime_number.s(i) for i in range(1,11))
    task_group.apply_async()
