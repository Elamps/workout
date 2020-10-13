from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Workout
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date

# Create your views here.

def home(request):
  return render(request, 'home.html')

@login_required
def workouts_index(request):
  workouts = Workout.objects.filter(user=request.user)
  most_recent_workout = Workout.objects.latest('date')
  current_date = date.today
  return render(request, 'workouts/index.html', { 'workouts': workouts, 'most_recent_workout': most_recent_workout, "current_date": current_date  })

@login_required
def workouts_detail(request, workout_id):
    workout = Workout.objects.get(id=workout_id)
    return render(request, 'workouts/detail.html', {'workout': workout})

class WorkoutCreate(LoginRequiredMixin, CreateView):
    model = Workout
    fields = ['name', 'description']
    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class WorkoutUpdate(LoginRequiredMixin, UpdateView):
    model = Workout
    fields = ['name', 'description']

class WorkoutDelete(LoginRequiredMixin, DeleteView):
  model = Workout
  success_url = '/workouts/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)