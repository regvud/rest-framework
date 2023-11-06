from django.urls import path

from .views import ParkCreateCarView, ParkListView, ParkRetrieveUpdateDestroyView

urlpatterns = [
    path("", ParkListView.as_view()),
    path("/<int:pk>", ParkRetrieveUpdateDestroyView.as_view()),
    path("/<int:pk>/create", ParkCreateCarView.as_view()),
]
