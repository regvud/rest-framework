from django.urls import path

from .views import ProfileListView, UserListCreateView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
    path('/profiles', ProfileListView.as_view(), name='profile_list'),
]
