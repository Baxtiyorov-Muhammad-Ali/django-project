import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from dashboard.consumers import ProductConsumer  # to'g'ri import qilish
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/products/", ProductConsumer.as_asgi()),  # WebSocket yo'li
        ])
    ),
})
