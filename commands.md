1) startproject - django-admin startproject dcelery
2) pip freeze > requirements.txt  --> To make the current installation to a new file
3) docker-compose up -d --build   --> To build a container with docker-compose and dockerfile config
4) function_name.delay()   --> To call a function with celery
5) docker exec -it django-dcelery /bin/sh   --> To intertact with the container
6) function_name.delay()   --> To call a celery task
7) task grouping
    from celery import group
    group_task = group(task1.s(),task2.s(),task3.s())
    group_task.delay()
    group_task.apply_async()    --> Will call all the grouped tasked at once and execute based on priority and parallely
8) task chaining
    from celery import chain
    chain_task = chain(task1.s(),task2.s(),task4.s(),task3.s())
    chain_task.apply_async()    --> Every task will run sequenntially, one after another, the output of one can be the input of another

9) # Remove all docker
    docker stop $(docker ps -aq) && docker rm $(docker ps -aq) && docker rmi $(docker images -aq)
    --> docker ps -aq list all the active container IDs
    --> docker images -aq list all the active images IDs
    --> docker rm and docker rmi will remove the container and the images

10) celery insepct active   --> Will return active tasks details
                    Sample  --> * {'id': 'a05c7068-f0aa-4d72-8a43-25fd3c0485f8', 'name': 'dcelery.celery.t1', 'args': [50, 80], 'kwargs': {'message': 'Multiplication of two numbers is'}, 'type': 'dcelery.celery.t1', 'hostname': 'celery@9a39c0a8c2c1', 'time_start': 1730861232.7648523, 'acknowledged': False, 'delivery_info': {'exchange': '', 'routing_key': 'tasks', 'priority': 9, 'redelivered': False}, 'worker_pid': 9}
11) celery inspect active_queues   --> will return active queues





DEFAULT SHELL IMPORTS

from dcelery.celery import *
from newapp.tasks import *
d = {"message": "Multiplication of two numbers is"}
t1.apply_async(args=[10,11],kwargs=d,priority=9)
t2.apply_async()
t3.apply_async()
t1.apply_async(args=[18,11],kwargs=d,priority=9)
t2.apply_async()
t3.apply_async()
t1.apply_async(args=[13,11],kwargs=d,priority=9)
t2.apply_async()
t3.apply_async()
t1.apply_async(args=[10,16],kwargs=d,priority=9)
t2.apply_async()
t3.apply_async()
t1.apply_async(args=[10,51],kwargs=d,priority=9)
t2.apply_async()
t3.apply_async()
t1.apply_async(args=[10,81],kwargs=d,priority=9)
t2.apply_async()
t3.apply_async()
t1.apply_async(args=[90,11],kwargs=d,priority=9)
t2.apply_async()
t3.apply_async()
t1.apply_async(args=[102,11],kwargs=d,priority=9)
t2.apply_async()
t3.apply_async()