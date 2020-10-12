from django.shortcuts import render, redirect
from .models import Workout
from django.views.generic import ListView, DetailView

# Create your views here.

def home(request):
  return render(request, 'home.html')

def workouts_index(request):
  return render(request, 'workouts/index.html', { 'workouts': workouts })

def workouts_detail(request, workout_id):
    workout = Workout.objects.get(id=workout_id)
    return render(request, 'workouts/detail.html', {'workout': workout})