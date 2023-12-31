from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_images/')
    label = models.CharField(max_length=100)
    content = models.TextField()
    readers = models.ManyToManyField(User, blank=True, related_name='blog_articles_read')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
