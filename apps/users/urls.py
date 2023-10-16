from django.urls import path

from apps.users.views import UserListCreateView, UserParkCreateView, UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='users_list'),
    path('<int:pk>', UserRetrieveUpdateDestroyAPIView.as_view(), name='user_crud'),
    path('<int:pk>/create_park', UserParkCreateView.as_view(), name='user_create_park'),

]
