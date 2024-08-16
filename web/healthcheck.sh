#!/bin/sh
python manage.py check --database default
python manage.py test_redis_con