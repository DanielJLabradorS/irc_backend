web: daphne irc_backend.asgi:application --port $PORT --bind 0.0.0.0 -v2
chatworker: python manage.py runworker channels --settings=irc_backend.settings -v2