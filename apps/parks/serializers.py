from rest_framework import serializers

from apps.parks.models import ParkModel


class ParkSerialiser(serializers.ModelSerializer):
    class Meta:
        model = ParkModel
        fields = ("id", "park_name")
