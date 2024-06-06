from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return HttpResponse(f'<h1>Welcome to random games!</h1>')

def oreshka(request):
    return HttpResponse(f"It is {random.choice(['Орёл','Решка'])}")

def dice(request):
    return HttpResponse(f'Dice sets to: {random.randint(1, 6)}')

def random_number(request):
    return HttpResponse(f'The number is: {random.randint(1, 100)}')

