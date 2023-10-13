from django.db import models

# Create your models here.
class Payments(models.Model):
    username = models.CharField(max_length=250)
    amount_money = models.IntegerField()
    # comment = models.CharField(max_length=250, bool = True, )
    # я забыл как там
