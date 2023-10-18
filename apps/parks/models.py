from django.db import models

from core.models import BaseModel


# Create your models here.
class ParkModel(BaseModel):
    class Meta:
        db_table = 'parks'

    park = models.CharField(max_length=30, unique=True)
