from rest_framework import serializers

from apps.parks.serializers import ParkCarsExcludedSerializer
from apps.users.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    parks = ParkCarsExcludedSerializer(read_only=True, many=True)

    class Meta:
        model = UserModel
        fields = ('id', 'user_name', 'user_age', 'user_status', 'parks')
