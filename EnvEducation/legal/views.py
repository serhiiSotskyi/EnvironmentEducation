from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def privacyPolicy(request):
    return render(request, "legal/privacyPolicy.html")

def termsOfUse(request):
    return render(request, "legal/termsOfUse.html")
