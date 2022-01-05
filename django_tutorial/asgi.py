"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
from django.core.asgi import get_asgi_application

import chat.routing
from chat.consumers import PrintConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_tutorial.settings')

application =  ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(chat.routing.websocket_urlpatterns)
    ),
    'channel': ChannelNameRouter({
        'test-print': PrintConsumer.as_asgi()
    })
})
