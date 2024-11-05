1) startproject - django-admin startproject dcelery
2) pip freeze > requirements.txt  --> To make the current installation to a new file
3) docker-compose up -d --build   --> To build a container with docker-compose and dockerfile config
4) function_name.delay()   --> To call a function with celery
5) docker exec -it django-dcelery /bin/sh   --> To intertact with the container