from django.contrib import admin
from .models import Article

# Customizing the appearance of the Article model in the Django admin interface
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'label', 'content')  # Display these fields in the list view
    list_filter = ('label',)  # Add a filter sidebar for the 'label' field

# Registering the Article model with the custom admin options
admin.site.register(Article, ArticleAdmin)
