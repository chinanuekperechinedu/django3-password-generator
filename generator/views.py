from django.shortcuts import render
from random import choice

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):

    character = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.GET.get('length'))

    thepassword = ''

    if (request.GET.get('uppercase')):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if (request.GET.get('numbers')):
        character.extend(list('1234567890'))

    if (request.GET.get('special')):
        character.extend(list('~!@#$%^&*()_+'))

    for i in range(length):
        thepassword += choice(character)

    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')
