from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request, "educationalMaterials/index.html", {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    # Mark the article as read for the current user
    article.readers.add(request.user)
    return render(request, 'educationalMaterials/article_detail.html', {'article': article})