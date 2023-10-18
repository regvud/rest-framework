from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


# Create your views here.
class CarListCreateView(generics.ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = (IsAuthenticated,)
