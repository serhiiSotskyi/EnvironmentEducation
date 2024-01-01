from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 

class RegisterUserForm(UserCreationForm):
    # Adding email field with appropriate widget and class for styling
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    # Adding first name field with appropriate widget and class for styling
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    # Adding last name field with appropriate widget and class for styling
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        # Including additional fields in the form
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        # Adding class to the username field for styling
        self.fields['username'].widget.attrs['class'] = 'form-control'
        # Adding class to the first password field for styling
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        # Adding class to the second password field for styling
        self.fields['password2'].widget.attrs['class'] = 'form-control'
