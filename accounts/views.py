from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_page(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        
        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Username does not exist')
            return redirect('/login/')
        
        user = authenticate(username = username, password = password)
        
        if user is None:
            messages.error(request, 'Invalid password')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/home/')
            
        
        
    return render(request, 'login.html')

def register_page(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        password = data.get('password')
        
        user = User.objects.filter(username = username)
        if user.exists():
            messages.error(request, "Username already exists")
            return redirect('/register/')
        
        user = User.objects.create(
            first_name = first_name, 
            last_name = last_name,
            username = username
        )
        
        user.set_password(password)
        user.save()
        
        messages.error(request, "Account created successfully")

        
        return redirect('/register')
    return render(request, 'register.html')


@login_required(login_url="/login/")
def home(request):
    return render(request, 'index.html')

def logout_page(request):
    logout(request)
    return redirect('/login')