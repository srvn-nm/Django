from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Hi. This is my home page.')