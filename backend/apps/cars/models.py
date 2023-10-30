from core.models import BaseModel

from django.db import models


# Create your models here.
class CarModel(BaseModel):
    class Meta:
        db_table = "cars"

    brand = models.CharField(max_length=20)
    year = models.IntegerField()
    price = models.IntegerField()
