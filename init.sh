#! /bin/bash

cd /opt/benroesler.com
# pip install --no-cache-dir -r requirements.txt

# pip install -r requirements.txt
python manage.py collectstatic; sleep 10
gunicorn --workers=2 --bind=0.0.0.0:8000 benroesler.wsgi