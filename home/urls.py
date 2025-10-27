from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('play/', views.say_hello),
    path('home/detail/todo/', views.detail),
    
]