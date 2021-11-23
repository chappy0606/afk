from functools import total_ordering
from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Quality(models.Model):
    type = models.CharField(max_length=20)


class Relic(models.Model):
    name = models.CharField(max_length=50)
    quality = models.ForeignKey(Quality, on_delete=models.CASCADE)
    compornent1 = models.ForeignKey('self',blank=True,null=True)
    compornent2 = models.ForeignKey('self', blank=True, null=True)
    compornent3 = models.ForeignKey('self', blank=True, null=True)
    compornent4 = models.ForeignKey('self', blank=True, null=True)
    cost = models.IntegerField(validators=MinValueValidator(0))
    total_price = models.IntegerField(validators=MinValueValidator(0))
