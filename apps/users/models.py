from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators as v
from django.db import models

from core.enum.enum_regexp import RegExp
from core.models import BaseModel

from .managers import UserManager


class ProfileModel(BaseModel):
    class Meta:
        db_table = 'profiles'

    name = models.CharField(max_length=20, validators=[v.RegexValidator(*RegExp.PROFILE.value)])
    surname = models.CharField(max_length=20, validators=[v.RegexValidator(*RegExp.PROFILE.value)])
    age = models.IntegerField(validators=[v.MinValueValidator(1), v.MaxValueValidator(100)])


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = 'auth_users'
        ordering = ('id',)

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, validators=[v.RegexValidator(*RegExp.PASSWORD.value)])
    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    profile = models.OneToOneField(ProfileModel, on_delete=models.CASCADE, related_name='user', null=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()
