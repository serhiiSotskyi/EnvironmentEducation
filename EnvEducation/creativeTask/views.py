from django.shortcuts import render
from .models import IdeaSubmission
from .forms import IdeaSubmissionForm
from django.contrib import messages

def index(request):
    # Initialize variables for submitted data and submission status
    submitted_data = None
    submitted = False

    # Check if the form is submitted
    if request.method == 'POST':
        # Create an instance of the IdeaSubmissionForm with POST data
        form = IdeaSubmissionForm(request.POST, request.FILES)
        
        # Check if the form is valid
        if form.is_valid():
            # Save the form data to the database
            form.save()
            
            # Retrieve cleaned data from the form
            submitted_data = form.cleaned_data
            
            # Set the submission status to True
            submitted = True
            
            # Create a new instance of the form for a new submission
            form = IdeaSubmissionForm()
            
            # Display a success message
            messages.success(request, ("Your post was submitted successfully!"))
    else:
        # If the form is not submitted, create a new instance of the form
        form = IdeaSubmissionForm()
    
    # Retrieve all submitted data from the database
    submitted_data = IdeaSubmission.objects.all()
    
    # Render the HTML template with form, submitted data, and submission status
    return render(request, "creativeTask/index.html", {'form': form, 'submitted_data': submitted_data, 'submitted': submitted})
