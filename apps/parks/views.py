from rest_framework import generics

from apps.parks.serializers import ParkSerialiser

from .models import ParkModel


class ParkListView(generics.ListAPIView):
    queryset = ParkModel.objects.all()
    serializer_class = ParkSerialiser


class ParkRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParkModel
    serializer_class = ParkSerialiser
