# benroesler.com
Personal website built with Django and Bootstrap, being served by nginx

# Docker Setup (Preferred Method)

sudo docker build . -t benroesler.com
sudo docker run -t -i -d -p 8000:8000 --restart always --name benroesler.com --rm benroesler.com
