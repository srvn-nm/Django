from django.shortcuts import render, HttpResponse

# Create your views here.
def Profile(request, username):
    return HttpResponse(f'This is {username}\'s profile page.')