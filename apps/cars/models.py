from django.db import models

from apps.parks.models import ParkModel

from core.models import BaseModel


# Create your models here.
class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=20)
    year = models.IntegerField()
    price = models.IntegerField()
    park_name = models.ForeignKey(ParkModel, on_delete=models.CASCADE, related_name='park_cars')
