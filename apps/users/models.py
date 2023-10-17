from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from core.models import BaseModel


class ProfileModel(BaseModel):
    class Meta:
        db_table = 'profiles'

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = 'auth_users'

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    profile = models.OneToOneField(ProfileModel, on_delete=models.CASCADE, related_name='user', null=True)

    USERNAME_FIELD = 'email'
