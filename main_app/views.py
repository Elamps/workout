from django.shortcuts import render, redirect

# Create your views here.

def home(request):
  return render(request, 'home.html')

def workouts_index(request):
  return render(request, 'workouts/index.html', { 'workouts': workouts })