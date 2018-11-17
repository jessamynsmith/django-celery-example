web: gunicorn django_celery_example.wsgi:application -b 0.0.0.0:$PORT -w 5

worker: celery -A django_celery_example worker -l info --without-gossip --without-mingle --without-heartbeat
