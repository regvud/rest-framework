from django.db import models

from core.models import BaseModel


# Create your models here.
class ParkModel(BaseModel):
    class Meta:
        db_table = "PARKS"
        ordering = ("id",)

    park_name = models.CharField(max_length=120)
