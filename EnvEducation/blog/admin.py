from django.contrib import admin
from .models import Article

# Customizing the display of Article model in the Django admin interface
class ArticleAdmin(admin.ModelAdmin):
    # Displayed columns in the change list view
    list_display = ('title', 'label', 'content')
    
    # Adding a filter option based on the 'label' field
    list_filter = ('label',)

# Registering the Article model with the custom admin configuration
admin.site.register(Article, ArticleAdmin)
