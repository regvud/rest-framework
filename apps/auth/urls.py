from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RecoverPasswordView, ShowMeView

urlpatterns = [
    path("", TokenObtainPairView.as_view()),
    path("/refresh", TokenRefreshView.as_view()),
    path("/me", ShowMeView.as_view()),
    path("/recover/<int:pk>", RecoverPasswordView.as_view()),
]
