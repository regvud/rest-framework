from rest_framework import generics

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


class CarListCreateView(generics.ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
