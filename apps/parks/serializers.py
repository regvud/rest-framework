from rest_framework import serializers

from apps.cars.serializers import CarSerializer
from apps.parks.models import ParkModel


class ParkSerializer(serializers.ModelSerializer):
    park_cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = ParkModel
        fields = ('id', 'park_name', 'park_cars')