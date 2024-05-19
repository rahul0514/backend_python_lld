from django.db import models

from ecomdemo.models import User


class Products(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=100)
    stock = models.IntegerField()