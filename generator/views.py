from django.shortcuts import render
from django.http import HttpResponse
import random
import string

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    password = ''
    characters = list(string.ascii_lowercase) # string.ascii_lowercase return this 'abcdefghijklmnopqrstuvwxyz'

    if (request.GET.get('uppercase')):
        characters.extend(list(string.ascii_uppercase))
    
    if (request.GET.get('specialcharacters')):
        characters.extend(list('@$%&*()!'))

    if (request.GET.get('numbers')):
        characters.extend(list(string.digits))
    
    length = int(request.GET.get('length', 12))

    for x in range(length):
        password += random.choice(characters)

    return render(request, 'generator/password.html', { 'password': password })

def about(request):
    return render(request, 'generator/about.html')
