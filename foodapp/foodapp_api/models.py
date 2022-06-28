from django.db import models

# Create your models here.

class Food(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=100)
    price = models.CharField(max_length=8)
    date = models.DateField()