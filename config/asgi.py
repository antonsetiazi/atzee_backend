# config/asgi.py

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from core.realtime.middleware import JWTAuthMiddleware
from django.core.asgi import get_asgi_application

import core.realtime.routing

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        JWTAuthMiddleware(
            URLRouter(
                core.realtime.routing.websocket_urlpatterns
            )
        )
    ),
})
