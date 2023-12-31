# forms.py
from django import forms
from .models import *

class IdeaSubmissionForm(forms.ModelForm):
    class Meta:
        model = IdeaSubmission
        fields = ['name', 'name_of_the_idea', 'text', 'drawing_file']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'name_of_the_idea': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'drawing_file': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
