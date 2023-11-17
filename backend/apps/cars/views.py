from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer
from rest_framework import generics


class CarListCreateView(generics.ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


class CarRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarModel
    serializer_class = CarSerializer
