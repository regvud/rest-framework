from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer

from core.permissions import IsAdminOrWriteOnly


# Create your views here.
class CarListView(generics.ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = (IsAuthenticated,)


class CarRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = (IsAdminOrWriteOnly,)
