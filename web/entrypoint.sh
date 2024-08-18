#!/bin/sh
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb

python manage.py collectstatic --noinput
python manage.py createsuperuser --noinput

python manage.py runserver 0:8000