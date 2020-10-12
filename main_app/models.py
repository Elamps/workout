from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
class Workout(models.Model):
    date = models.DateField('workout date')
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'workout_id': self.id})
