web: python manage.py migrate && python manage.py loaddata data_export.json 2>/dev/null || true && python manage.py collectstatic --noinput && gunicorn sa_doj.wsgi:application --bind 0.0.0.0:$PORT

