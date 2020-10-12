from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('workouts/', views.workouts_index, name='index'),
    path('workouts/<int:workout_id>/', views.workouts_detail, name='detail'),
]