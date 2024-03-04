# homepage/views.py
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def dog(request):
    return render(request,'dog.html')
def cart(request):
    return render(request,'cart.html')





