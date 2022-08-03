from django.shortcuts import render, HttpResponse

users = ['Sarvin', 'Abtin', 'Nazanin', 'Mozhgan', 'Bahram']

blockedUsers = ['Sarvin']

# Create your views here.
def Profile(request, username):
    if username in users and username in blockedUsers:
        # return HttpResponse(f'This {username} is blocked. >-<')
        return render(request, 'accounts_app/profile.html')
    elif username in users:
        return HttpResponse(f'This is {username}\'s profile page. ^-^')
    elif username not in users:
        return HttpResponse(f'{username} is not a valid username. >-<')