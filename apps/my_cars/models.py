from django.db import models

from core.models import BaseModel


class CarModel(BaseModel):
    class Meta:
        db_table = 'my_cars'

    brand = models.CharField(max_length=20)
    year = models.IntegerField()
    price = models.IntegerField()
    engine_volume = models.FloatField()
