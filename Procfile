web: gunicorn application:app --log-file -
celery: celery worker -A application.celery --loglevel=info