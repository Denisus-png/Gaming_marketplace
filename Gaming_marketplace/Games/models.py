from django.db import models

# Create your models here.
class Games(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    creator = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    year = models.IntegerField()