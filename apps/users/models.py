from django.core import validators as v
from django.db import models

from apps.users.choices import StatusChoices

from core.emun.enum_Regexp import RegExp
from core.models import BaseModel


class UserModel(BaseModel):
    class Meta:
        db_table = 'users'

    user_name = models.CharField(max_length=20, validators=[v.RegexValidator(*RegExp.DEFAULT.value)])
    user_age = models.IntegerField(validators=[v.MinValueValidator(0), v.MaxValueValidator(100)])
    user_status = models.CharField(max_length=5, choices=StatusChoices.choices)
