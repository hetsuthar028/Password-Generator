from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    passwd = list('abcdefghijklmnopqrstuvwxyz')
    finalPass = ''
    if request.GET.get('uppercase'):
        passwd.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('specialcharacters'):
        passwd.extend(list('!@#$%^&*'))

    if request.GET.get('numbers'):
        passwd.extend(list('0123'))
    if request.GET.get('brackets'):
        passwd.extend(list("{}[](){}[]{}"))
    length = int(request.GET.get('length', 10))

    for x in range(length):
        finalPass += random.choice(passwd)
    return render(request, 'generator/password.html', {'password1': finalPass})

def about(request):
    return render(request, 'generator/aboutme.html')
