from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(f"Received form submission: Name - {name}, Email - {email}, Message - {message}")

        # Save the form submission to the database
        submission = ContactFormSubmission.objects.create(name=name, email=email, message=message)

        # Return a JSON response to indicate success
        return JsonResponse({'status': 'success', 'submission_id': submission.id})

    return render(request, "main/index.html")

def submit_form(request):
    if request.method == 'POST':
        # Process form data
        data = json.loads(request.body)
        name = data.get('name')
        # Process other form fields

        # Do something with the data, e.g., save to the database

        return JsonResponse({'status': 'success', 'message': 'Form submitted successfully'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})