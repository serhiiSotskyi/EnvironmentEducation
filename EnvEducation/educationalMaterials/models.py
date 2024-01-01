from django.db import models
from django.contrib.auth.models import User

# Article model to represent educational materials
class Article(models.Model):
    title = models.CharField(max_length=100)  # Title of the article
    image = models.ImageField(upload_to='article_images/')  # Image associated with the article
    label = models.CharField(max_length=100)  # Label of the article
    content = models.TextField()  # Text content of the article
    readers = models.ManyToManyField(User, blank=True, related_name='edu_articles_read')  # Many-to-Many relationship with User model for tracking readers

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save method to handle model-specific behavior during save
