# Build
## sudo docker build . -t benroesler.com

# Run
## sudo docker run -t -i -d -p 8000:8000 --name benroesler.com --rm benroesler.com
FROM python:latest

LABEL maintainer="Benny Roesler <bennytroesler@gmail.com>"

COPY ./app /app
RUN ls /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app
EXPOSE 8000

CMD ["sh","/app/init.sh"]