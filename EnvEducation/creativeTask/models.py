from django.db import models

class IdeaSubmission(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    text = models.TextField(blank=True)
    drawing_file = models.FileField(upload_to='drawing_files/', blank=True, null=True)

    def __str__(self):
        return self.name
