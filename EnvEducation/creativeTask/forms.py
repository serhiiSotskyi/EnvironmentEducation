from django import forms
from .models import *

# Define a form for IdeaSubmission model
class IdeaSubmissionForm(forms.ModelForm):
    class Meta:
        # Use the IdeaSubmission model
        model = IdeaSubmission
        # Specify the fields to include in the form
        fields = ['name', 'name_of_the_idea', 'text', 'drawing_file']
        # Define widgets to customize the appearance of form fields
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'name_of_the_idea': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'drawing_file': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
