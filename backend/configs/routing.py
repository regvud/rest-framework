from apps.chat.routing import websocketpatterns as chat_router
from channels.routing import URLRouter
from django.urls import path

websocket_urlpatterns = [
    path("api/chat/", URLRouter(chat_router)),
]
