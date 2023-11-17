from apps.cars.models import CarModel
from rest_framework import serializers


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ("id", "brand", "year", "price")
