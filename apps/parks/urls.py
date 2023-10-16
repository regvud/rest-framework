from django.urls import path

from apps.parks.views import ParkCreateCarView, ParkListView, ParkRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', ParkListView.as_view(), name='park_list'),
    path('<int:pk>', ParkRetrieveUpdateDestroyAPIView.as_view(), name='park_crud'),
    path('<int:pk>/create', ParkCreateCarView.as_view(), name='park_create_car'),

]
