from rest_framework import generics, status
from rest_framework.response import Response

from apps.my_cars.serializers import CarSerializer
from apps.parks.models import ParkModel
from apps.parks.serializers import ParkSerializer


# Create your views here.
class ParkListCreateView(generics.ListCreateAPIView):
    serializer_class = ParkSerializer
    queryset = ParkModel.objects.all()


class ParkRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ParkSerializer
    queryset = ParkModel.objects.all()


class ParkCreateCarView(generics.CreateAPIView):
    queryset = ParkModel.objects.all()

    def post(self, request, *args, **kwargs):
        park = self.get_object()
        car = self.request.data
        serializer = CarSerializer(data=car)
        serializer.is_valid(raise_exception=True)
        serializer.save(park=park)
        return Response(serializer.data, status.HTTP_201_CREATED)
