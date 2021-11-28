from django.db import models
import uuid
from django.core.validators import MinValueValidator

# Create your models here.
class Quality(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type


def rename_to_uuid(self, filename):
    prefix = 'relics/'
    return prefix + str(uuid.uuid4()).replace('-', '') + ".png"

class Relic(models.Model):
    en_name = models.CharField(max_length=50)
    ja_name = models.CharField(max_length=50)
    quality = models.ForeignKey(Quality, on_delete=models.CASCADE)
    compornent1 = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.SET_NULL, related_name='compornent1_relic')
    compornent2 = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.SET_NULL, related_name='compornent2_relic')
    compornent3 = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.SET_NULL, related_name='compornent3_relic')
    compornent4 = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.SET_NULL, related_name='compornent4_relic')
    cost = models.IntegerField(validators=[MinValueValidator(0)])
    total_price = models.IntegerField(validators=[MinValueValidator(0)])
    icon = models.ImageField(upload_to=rename_to_uuid, null=True)