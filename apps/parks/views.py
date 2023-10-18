from rest_framework import generics
from rest_framework.response import Response

from apps.cars.serializers import CarSerializer
from apps.parks.models import ParkModel
from apps.parks.serializers import ParkSerializer


# Create your views here.
class ParkListCreateView(generics.ListCreateAPIView):
    serializer_class = ParkSerializer
    queryset = ParkModel.objects.all()


class ParkRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ParkSerializer
    queryset = ParkModel


class ParkCreateCarView(generics.GenericAPIView):
    queryset = ParkModel.objects.all()

    def post(self, *args, **kwargs):
        park = self.get_object()
        car = self.request.data
        serializer = CarSerializer(data=car)
        serializer.is_valid(raise_exception=True)
        serializer.save(park=park)
        return Response(serializer.data, status=201)
