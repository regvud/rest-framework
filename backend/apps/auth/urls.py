from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    RecoverPasswordRequestView,
    RecoverPasswordView,
    ShowMeView,
    SocketView,
)

urlpatterns = [
    path("", TokenObtainPairView.as_view()),
    path("/refresh", TokenRefreshView.as_view()),
    path("/me", ShowMeView.as_view()),
    path("/recover", RecoverPasswordRequestView.as_view()),
    path("/recover/<str:token>", RecoverPasswordView.as_view()),
    path("/socket", SocketView.as_view()),
]
