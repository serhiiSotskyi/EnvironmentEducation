from django.db import models
from django.contrib.auth.models import User

# Model representing an article in the blog
class Article(models.Model):
    # Title of the article
    title = models.CharField(max_length=100)

    # Image associated with the article, stored in the 'blog_images/' directory
    image = models.ImageField(upload_to='blog_images/')

    # Label categorizing the article
    label = models.CharField(max_length=100)

    # Content of the article
    content = models.TextField()

    # Many-to-many relationship with the User model, representing readers of the article
    readers = models.ManyToManyField(User, blank=True, related_name='blog_articles_read')

    # Custom save method to handle additional logic when saving an article
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
