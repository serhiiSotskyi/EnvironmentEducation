from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def logIn_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:index')
            
        else:
            messages.success(request, ("There was an Error Logging In, Try again..."))
            return redirect('log:logIn_user')      
    else:
        return render(request, "authenticate/logIn.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out"))
    return redirect('main:index')

def signUp_user(request):
    return render(request, "log/signUp.html")
