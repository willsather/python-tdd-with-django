from django.db import models

# Create your models here.

class Penguin(models.Model):
    island = models.CharField(max_length=50)
    body_mass = models.IntegerField()
    gender = models.CharField(max_length=6)
