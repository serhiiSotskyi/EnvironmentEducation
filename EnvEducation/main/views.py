from django.shortcuts import render
from .models import ContactFormSubmission

def index(request):
    # Check if the request method is POST, indicating a form submission
    if request.method == 'POST':
        # Create an instance of ContactFormSubmission
        contact = ContactFormSubmission()

        # Retrieve data from the POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Set the attributes of the ContactFormSubmission instance
        contact.name = name
        contact.email = email
        contact.message = message

        # Save the form submission to the database
        contact.save()

    # Render the index.html template
    return render(request, "main/index.html")
