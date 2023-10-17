from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.my_cars.models import CarModel
from apps.my_cars.serializers import CarSerializer


# Create your views here.
class CarListView(generics.ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = (IsAuthenticated,)


class CarRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
