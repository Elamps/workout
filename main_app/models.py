from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Workout(models.Model):
    date = models.DateField('workout date')
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'workout_id': self.id})
    
    class Meta:
        ordering = ['-date']
    
    def worked_out_today(self):
        return date.today() == self.date

