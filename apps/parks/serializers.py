from rest_framework import serializers

from apps.my_cars.serializers import CarSerializer
from apps.parks.models import ParkModel


class ParkSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = ParkModel
        fields = ('park_name', 'cars')
