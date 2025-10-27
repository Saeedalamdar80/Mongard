from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('detail/<int:todo_id>/', views.detail, name= 'details'), # url dispatcher
    path('delete/<int:todo_id>/', views.delete, name='delete'),
]