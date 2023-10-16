from datetime import datetime

from django.core import validators as v
from django.db import models

from apps.parks.models import ParkModel

from core.emun.enum_Regexp import RegExp
from core.models import BaseModel


class CarModel(BaseModel):
    class Meta:
        db_table = 'my_cars'
        ordering = ['id']

    brand = models.CharField(max_length=20, validators=[v.RegexValidator(*RegExp.DEFAULT.value)])
    year = models.IntegerField(
        validators=[v.MinValueValidator(1950), v.MaxValueValidator(datetime.now().year)])
    price = models.IntegerField(validators=[v.MinValueValidator(100), v.MaxValueValidator(10000000)])
    engine_volume = models.FloatField(validators=[v.MinValueValidator(0.8), v.MaxValueValidator(12)])
    park = models.ForeignKey(ParkModel, on_delete=models.CASCADE, related_name='cars')
