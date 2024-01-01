from django.contrib import admin
from .models import ContactFormSubmission

# Register the ContactFormSubmission model with the Django admin.
# This allows to manage and view instances of ContactFormSubmission in the admin interface.
admin.site.register(ContactFormSubmission)