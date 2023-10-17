from django.urls import path

from apps.my_cars.views import CarListView, CarRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('<int:pk>', CarRetrieveUpdateDestroyAPIView.as_view(), name='car_crud'),
]
