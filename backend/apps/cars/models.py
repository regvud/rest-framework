from apps.parks.models import ParkModel
from core.models import BaseModel
from django.db import models


# Create your models here.
class CarModel(BaseModel):
    class Meta:
        db_table = "CARS"
        ordering = ("id",)

    brand = models.CharField(max_length=120)
    year = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
