from django.urls import path

from .views import ParkCreateCarView, ParkListCreateView, ParkRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', ParkListCreateView.as_view(), name='park_list_create'),
    path('/<int:pk>', ParkRetrieveUpdateDestroyAPIView.as_view(), name='park_crud'),
    path('/<int:pk>/create_car', ParkCreateCarView.as_view(), name='park_create_car'),
]
