from django.urls import path

from .views import ParkListView, ParkRetrieveUpdateDestroyView

urlpatterns = [
    path("", ParkListView.as_view()),
    path("/<int:pk>", ParkRetrieveUpdateDestroyView.as_view()),
]
