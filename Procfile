web: gunicorn shegar.wsgi:application --bind 0.0.0.0:$PORT --workers 3
release: python manage.py migrate && python manage.py collectstatic --noinput