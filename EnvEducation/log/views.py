from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def logIn(request):
    return render(request, "log/logIn.html")

def signUp(request):
    return render(request, "log/signUp.html")
