from django.contrib.auth import login
from django.shortcuts import render, redirect



def signup(request):
         return render(request, 'signup.html',)

def home(request):
        return render(request, 'homepage.html',)

def first(request):
    return render(request, 'firstpage.html',)

def gallery(request):
    return render(request, 'gallery.html',)
# Create your views here.
def login(request):
    return render(request, 'login.html', )
