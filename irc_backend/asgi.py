"""
ASGI config for irc_backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'irc_backend.settings')
channel_layer = channels.asgi.get_channel_layer()

application = get_asgi_application()
