from rest_framework import serializers

from apps.my_cars.models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('brand', 'year', 'price', 'engine_volume')
