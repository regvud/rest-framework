from django.contrib.auth import get_user_model

from rest_framework import serializers

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_superuser', 'is_staff', 'is_active', 'last_login', 'created_at',
            'updated_at')
        read_only = ('id', 'is_superuser', 'is_staff', 'is_active', 'created_at', 'updated_at')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user
