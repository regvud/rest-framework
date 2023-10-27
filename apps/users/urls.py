from django.urls import path

from .views import UserListCreateView, UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('/<int:pk>', UserRetrieveUpdateDestroyAPIView.as_view()),
]
