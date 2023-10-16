from rest_framework import generics

from apps.my_cars.filters import CarFilter
from apps.my_cars.models import CarModel
from apps.my_cars.serializers import CarSerializer


# Create your views here.
class CarListView(generics.ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    filterset_class = CarFilter


class CarRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
