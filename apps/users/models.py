from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from core.models import BaseModel

from .managers import UserManager


class ProfileModel(BaseModel):
    class Meta:
        db_table = 'profiles'
        ordering = ('id',)

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.CharField(max_length=20)


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = 'auth_users'
        ordering = ('id',)

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    profile = models.OneToOneField(ProfileModel, on_delete=models.CASCADE, related_name='user', null=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()
