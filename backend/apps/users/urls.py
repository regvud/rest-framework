from django.urls import path

from .views import UserListCreateView, UserRetrieveDestroyView

urlpatterns = [
    path("", UserListCreateView.as_view()),
    path("/<int:pk>", UserRetrieveDestroyView.as_view()),
]
