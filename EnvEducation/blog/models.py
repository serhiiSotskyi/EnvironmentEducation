from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='article_images/')
    label = models.CharField(max_length=100)
    content = models.TextField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Automatically create a URL for the article detail page
        self.url = reverse('blog:article_detail', args=[str(self.id)])
        super().save(*args, **kwargs)