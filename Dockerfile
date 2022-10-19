FROM python:3.10

LABEL maintainer="Peter Gichia <petergichia35@gmail.com>"

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN pip install --upgrade pip && pip install gunicorn==20.1.0

COPY ./docker-files/start.sh /start.sh
RUN chmod +x /start.sh

COPY ./docker-files/gunicorn_conf.py /gunicorn_conf.py

COPY ./docker-files/start-reload.sh /start-reload.sh
RUN chmod +x /start-reload.sh

COPY ./ /app
COPY ./docker-files/prestart.sh /app
WORKDIR /app/

ENV PYTHONPATH=/app

EXPOSE 80

# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Gunicorn with Uvicorn
CMD ["/start.sh"]