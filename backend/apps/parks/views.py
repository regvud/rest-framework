from apps.cars.serializers import CarSerializer
from apps.parks.serializers import ParkSerialiser
from rest_framework import generics, status
from rest_framework.response import Response

from .models import ParkModel


class ParkListView(generics.ListCreateAPIView):
    queryset = ParkModel.objects.all()
    serializer_class = ParkSerialiser   


class ParkRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParkModel
    serializer_class = ParkSerialiser


class ParkCreateCarView(generics.GenericAPIView):
    queryset = ParkModel.objects.all()

    def post(self, *args, **kwargs):
        park = self.get_object()
        car = self.request.data
        serializer = CarSerializer(data=car)
        serializer.is_valid(raise_exception=True)
        serializer.save(park=park)

        return Response(serializer.data, status.HTTP_201_CREATED)
