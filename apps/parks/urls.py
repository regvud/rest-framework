from django.urls import path

from .views import ParkCreateCarView, ParkListCreateView, ParkRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', ParkListCreateView.as_view()),
    path('/<int:pk>', ParkRetrieveUpdateDestroyAPIView.as_view()),
    path('/<int:pk>/create_car', ParkCreateCarView.as_view())
]
