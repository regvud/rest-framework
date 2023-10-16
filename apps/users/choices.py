from django.db import models


class StatusChoices(models.TextChoices):
    TRUE = 'true'
    FALSE = 'false'
