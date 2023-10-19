from django.urls import path

from .views import CarListView, CarRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('/<int:pk>', CarRetrieveUpdateDestroyAPIView.as_view(), name='car_list')
]
