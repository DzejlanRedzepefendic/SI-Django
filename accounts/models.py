from django.db import models

# Create your models here.
class Accounts(models.Model):
    wallet = models.IntegerField(null = True)
    full_name = models.CharField(max_length=30)