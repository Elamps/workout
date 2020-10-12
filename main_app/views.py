from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Workout
from django.views.generic import ListView, DetailView

# Create your views here.

def home(request):
  return render(request, 'home.html')

def workouts_index(request):
  workouts = Workout.objects.all()
  return render(request, 'workouts/index.html', { 'workouts': workouts })

def workouts_detail(request, workout_id):
    workout = Workout.objects.get(id=workout_id)
    return render(request, 'workouts/detail.html', {'workout': workout})

class WorkoutCreate(CreateView):
    model = Workout
    fields = '__all__'
    success_url = '/'

class WorkoutUpdate(UpdateView):
    model = Workout
    fields = ['name', 'description']

class WorkoutDelete(DeleteView):
  model = Workout
  success_url = '/workouts/'