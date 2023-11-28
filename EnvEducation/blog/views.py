from django.http import HttpResponse
from .models import Article
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    return render(request, "blog/index.html")

def article1(request):
    return render(request, "blog/article1.html")

def article2(request):
    return render(request, "blog/article2.html")

def article3(request):
    return render(request, "blog/article3.html")

def article_list(request):
    articles = Article.objects.all()
    print("Check")
    print(articles)
    return render(request, 'blog/article_list.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog/article_detail.html', {'article': article})
