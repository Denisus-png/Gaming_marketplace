from django.db import models

# Create your models here.
class Games(models.Model):
    username = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    password = models.IntegerField()