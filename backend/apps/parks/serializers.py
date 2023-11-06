from rest_framework import serializers

from apps.cars.serializers import CarSerializer
from apps.parks.models import ParkModel


class ParkSerialiser(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = ParkModel
        fields = ("id", "park_name", "cars")
