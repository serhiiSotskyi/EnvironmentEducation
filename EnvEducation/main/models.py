from django.db import models

class ContactFormSubmission(models.Model):
    # Fields for storing information from the contact form submission
    name = models.CharField(max_length=255)  # Store the name of the person submitting the form
    email = models.EmailField()  # Store the email address of the person submitting the form
    message = models.TextField()  # Store the message content from the contact form
    submission_date = models.DateTimeField(auto_now_add=True)  # Store the date and time of the form submission

    def __str__(self):
        # Return a string representation of the ContactFormSubmission instance
        # This is useful for human-readable identification in the Django admin interface
        return f'{self.name} - {self.submission_date}'
