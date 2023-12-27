# forms.py
from django import forms
from .models import *

class IdeaSubmissionForm(forms.ModelForm):
    class Meta:
        model = IdeaSubmission
        fields = ['name', 'category', 'text', 'drawing_file']
