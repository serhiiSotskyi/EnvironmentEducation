from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm
from quiz.models import *

def logIn_user(request):
    # Handle user login
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You were logged in"))
            return redirect('main:index')
        else:
            messages.success(request, ("There was an Error Logging In, Try again..."))
            return redirect('log:logIn_user')
    else:
        # Render login form
        return render(request, "authenticate/logIn.html", {})

def logout_user(request):
    # Handle user logout
    logout(request)
    messages.success(request, ("You were logged out"))
    return redirect('main:index')

def signUp_user(request):
    # Handle user signup
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration is successful"))
            return redirect('main:index')
    else:
        form = RegisterUserForm()
    
    # Render signup form
    return render(request, "authenticate/signUp.html", {"form": form})
