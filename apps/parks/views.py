from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.permissions import IsAdminOrWriteOnly

from ..cars.serializers import CarSerializer
from .models import ParkModel
from .serializers import ParkSerializer


# Create your views here.
class ParkListCreateView(generics.ListCreateAPIView):
    serializer_class = ParkSerializer
    queryset = ParkModel.objects.all()

    def get_permissions(self, *args, **kwargs):
        if self.request.method == 'POST':
            pass


class ParkRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ParkSerializer
    queryset = ParkModel.objects.all()
    permission_classes = (IsAdminOrWriteOnly,)


class ParkCreateCarView(generics.CreateAPIView):
    queryset = ParkModel.objects.all()
    permission_classes = (IsAdminOrWriteOnly,)

    def post(self, request, *args, **kwargs):
        park_name = self.get_object()
        car = self.request.data
        serializer = CarSerializer(data=car)
        serializer.is_valid(raise_exception=True)
        serializer.save(park_name=park_name)
        return Response(serializer.data, status=201)
