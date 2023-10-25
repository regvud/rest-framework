from django.contrib.auth import get_user_model
from django.db.transaction import atomic

from rest_framework import serializers

from apps.users.models import ProfileModel

from core.services.email_service import EmailService

UserModel = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('id', 'name', 'surname', 'age')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_superuser', 'is_staff', 'is_active', 'last_login', 'created_at',
            'updated_at', 'profile')
        read_only = ('id', 'is_superuser', 'is_staff', 'is_active', 'last_login', 'created_at', 'updated_at')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    @atomic
    def create(self, validated_data):
        profile = validated_data.pop('profile')
        profile = ProfileModel.objects.create(**profile)
        user = UserModel.objects.create_user(profile=profile, **validated_data)
        EmailService.register_email(user)
        return user
