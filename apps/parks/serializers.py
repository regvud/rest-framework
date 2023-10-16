from rest_framework import serializers

from apps.my_cars.serializers import CarSerializer
from apps.parks.models import ParkModel


class ParkSerializer(serializers.ModelSerializer):
    cars = CarSerializer(read_only=True, many=True)

    class Meta:
        model = ParkModel
        fields = ('id', 'park_name', 'cars')


class ParkCarsExcludedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkModel
        fields = ('id', 'park_name')
