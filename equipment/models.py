from django.db import models

# Create your models here.
class Equipment(models.Model):
    computer = models.IntegerField()
    available = models.BooleanField(null=True)
