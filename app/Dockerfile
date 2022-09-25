# Build
## sudo docker build . -t benroesler.com

# Run
## sudo docker run -t -i -d -p 8000:8000 --name benroesler.com --rm benroesler.com
FROM python:3

COPY . /app/benroesler.com

WORKDIR /app/benroesler.com

RUN pwd; ls -la
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000 
CMD ["sh", "/app/benroesler.com/init.sh"]