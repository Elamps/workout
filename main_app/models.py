from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
class Workout(models.Model):
    date = models.DateField('workout date')
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    