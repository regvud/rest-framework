from django.urls import path

from .views import FromAdminToUserView, FromUserToAdminView, ProfileListView, UserBlockView, UserListCreateView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
    path('/profiles', ProfileListView.as_view(), name='profile_list'),
    path('/<int:pk>/user_to_admin', FromUserToAdminView.as_view(), name='user_to_admin'),
    path('/<int:pk>/admin_to_user', FromAdminToUserView.as_view(), name='admin_to_user'),
    path('/<int:pk>/block', UserBlockView.as_view(), name='block_user'),
]
