import os
import django
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import terminal.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # Just HTTP for now. (We can add other protocols later.)
    "websocket":AuthMiddlewareStack(
        URLRouter(
            terminal.routing.websocket_urlpatterns
        )
    )
})

