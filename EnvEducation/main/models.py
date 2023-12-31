from django.db import models

# Create your models here.
class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.submission_date}'