from django.shortcuts import render
from .models import Article
from django.shortcuts import render, get_object_or_404

def index(request):
    # Retrieve all articles
    articles = Article.objects.all()
    # Render the index page with the list of articles
    return render(request, "educationalMaterials/index.html", {'articles': articles})

def article_detail(request, article_id):
    # Retrieve the specific article with the given ID or return a 404 page if not found
    article = get_object_or_404(Article, pk=article_id)
    # Mark the article as read for the current user
    article.readers.add(request.user)
    # Render the article detail page with the specific article
    return render(request, 'educationalMaterials/article_detail.html', {'article': article})
