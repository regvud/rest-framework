from rest_framework import generics

from .models import CarModel
from .serializers import CarSerializer


class CarListCreateView(generics.ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
