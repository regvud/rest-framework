from django.db import models

from apps.users.models import UserModel

from core.models import BaseModel


# Create your models here.
class ParkModel(BaseModel):
    class Meta:
        db_table = 'parks'

    park_name = models.CharField(max_length=20)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='parks')
