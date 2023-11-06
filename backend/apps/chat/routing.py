from django.urls import path

from .consumers import ChatConsumer

websocketpatterns = [
    path("<str:room>/", ChatConsumer.as_asgi()),
]
