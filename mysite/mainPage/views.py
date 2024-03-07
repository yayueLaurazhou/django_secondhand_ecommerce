from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Category, Product
from .forms import SignupForm,LoginForm


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
            messages.success(request, ("User Created!"))
            return redirect('mainPage:index') 
    else: 
        form = SignupForm()
    return render(request, 'main/signup.html', {
        'form': form
    })

def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You Have Been Logged In!"))
            return redirect('mainPage:index')
    else: 
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form })

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('mainPage:index')

