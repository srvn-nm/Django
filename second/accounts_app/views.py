from django.shortcuts import render, HttpResponse

users = ['Sarvin', 'Abtin', 'Nazanin', 'Mozhgan', 'Bahram']

# Create your views here.
def Profile(request, username):
    if username in users:
        return HttpResponse(f'This is {username}\'s profile page. ^-^')
    else:
        return HttpResponse(f'{username} is not a valid username. >-<')