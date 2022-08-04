#! /bin/bash

cd /app
python manage.py collectstatic -c --noinput
gunicorn --workers=2 --bind=0.0.0.0:8000 benroesler.wsgi