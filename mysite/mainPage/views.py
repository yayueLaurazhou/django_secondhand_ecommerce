from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Category, Product
from .forms import SignupForm


def index(request):
    categories = Category.objects.all()
    return render(request, 'main/index.html', {
        'categories' : categories
    })


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/') 
    else: 
        form = SignupForm()
    return render(request, 'main/signup.html')

def login_user(request):
    return render(request, 'login.html')    
def logout_user(request):
    pass