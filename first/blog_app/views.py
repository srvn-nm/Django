from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Hi ^-^.I am Sarvin. Welcome to my page!')
