#!/bin/sh
python -m gunicorn web.wsgi:application --bind 0.0.0.0:8015 &