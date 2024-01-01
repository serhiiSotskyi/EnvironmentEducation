from django.db import models

# Define the IdeaSubmission model
class IdeaSubmission(models.Model):
    # Fields for the IdeaSubmission model
    name = models.CharField(max_length=100)
    name_of_the_idea = models.CharField(max_length=50)
    text = models.TextField(blank=True)
    drawing_file = models.FileField(upload_to='drawing_files/', blank=True, null=True)
    submission_date = models.DateTimeField(auto_now_add=True)

    # Define a human-readable representation of the model
    def __str__(self):
        return f'{self.name} - {self.submission_date}'
