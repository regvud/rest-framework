from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.urls import path

from .views import MeView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='get_tokens'),
    path('/refresh', TokenRefreshView.as_view(), name='get_refresh_token'),
    path('/me', MeView.as_view(), name='get_me'),
]
