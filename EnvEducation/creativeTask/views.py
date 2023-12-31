# views.py
from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import IdeaSubmission
from .forms import IdeaSubmissionForm
from django.contrib import messages

def index(request):
    submitted_data = None
    submitted = False

    if request.method == 'POST':
        form = IdeaSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            submitted_data = form.cleaned_data
            submitted = True
            form = IdeaSubmissionForm()
            messages.success(request, ("Your post was submitted successfully!"))
    else:
        form = IdeaSubmissionForm()
    submitted_data = IdeaSubmission.objects.all()
    return render(request, "creativeTask/index.html", {'form': form, 'submitted_data': submitted_data, 'submitted': submitted})
