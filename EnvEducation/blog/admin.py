# blog/admin.py
from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'label', 'content')
    list_filter = ('label',)

admin.site.register(Article, ArticleAdmin)
