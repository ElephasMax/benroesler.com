#! /bin/bash

cd /opt/benroesler.com
python manage.py collectstatic -c --noinput
gunicorn --workers=2 --bind=0.0.0.0:8000 benroesler.wsgi