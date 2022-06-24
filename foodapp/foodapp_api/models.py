from django.db import models

# Create your models here.

class Food(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField()
    image = models.CharField()
    price = models.CharField()
    extraoption = models.CharField()
    date = models.DateField()