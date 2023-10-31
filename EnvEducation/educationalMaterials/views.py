from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "educationalMaterials/index.html")

def page1(request):
    return render(request, "educationalMaterials/page1.html")
