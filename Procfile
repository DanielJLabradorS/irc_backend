release: python manage.py migrate
web: gunicorn irc_backend.wsgi --log-file -
worker: python manage.py runworker channels --settings=irc_backend.settings -v2