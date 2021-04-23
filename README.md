# personal_website
Personal website built with Django and Bootstrap, being served by nginx

# Docker Setup
This repo can become a submodule for my django-gunicorn-nginx project. See that repo for instructions


# Setup

## Clone Repository
1.  Clone repository 
2.  Make sure python3 and django are installed
3.  pip install -r requirements.txt


## Nginx
1. Install nginx
2. Copy resources/benroesler.conf to /etc/nginx/sites-available/
3. Symlink configuration to /etc/nginx/sites-enabled/
4. Restart Nginx service


## Service and Sockets
1. Move resources/benroesler.service and resources/benroesler.socket into /etc/systemd/system/
2. Enable the systemd service with systemd benroesler
3. Verify everything is up and running with systemd status benroesler
