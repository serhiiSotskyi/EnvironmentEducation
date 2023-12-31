from .models import Article
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'blog/article_list.html', {'articles': articles})

@login_required
def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    
    # Mark the article as read for the current user
    article.readers.add(request.user)

    return render(request, 'blog/article_detail.html', {'article': article})