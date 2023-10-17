from django.urls import path

from .views import UserCreateView, UserListView

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('/create', UserCreateView.as_view(), name='user_create'),
]
