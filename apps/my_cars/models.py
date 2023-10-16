from django.db import models

from apps.parks.models import ParkModel

from core.models import BaseModel


class CarModel(BaseModel):
    class Meta:
        db_table = 'my_cars'

    brand = models.CharField(max_length=20)
    year = models.IntegerField()
    price = models.IntegerField()
    engine_volume = models.FloatField()
    park = models.ForeignKey(ParkModel, on_delete=models.CASCADE, related_name='cars')
