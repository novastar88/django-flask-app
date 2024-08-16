#!/bin/sh
python manage.py collectstatic --noinput &
python manage.py createsuperuser --noinput &
python -m gunicorn web.wsgi:application --bind 0.0.0.0:8015