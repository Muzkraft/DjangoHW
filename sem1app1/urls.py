from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('oreshka/', views.oreshka, name='oreshka'),
    path('dice/', views.dice, name='throw dice'),
    path('random-number/', views.random_number, name='random number'),
]