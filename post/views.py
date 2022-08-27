from django.shortcuts import render
from .models import User, Post, Scrap

def home(request):
    return render(request, 'home.html')

def create(request):
    return render(request, 'create.html')