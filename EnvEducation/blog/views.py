from .models import Article
from django.shortcuts import render, get_object_or_404

# View to display the list of articles
def article_list(request):
    # Query all articles from the database
    articles = Article.objects.all()

    # Render the article list template with the retrieved articles
    return render(request, 'blog/article_list.html', {'articles': articles})

# View to display the details of a specific article
def article_detail(request, article_id):
    # Retrieve the article with the given ID or return a 404 response if not found
    article = get_object_or_404(Article, pk=article_id)
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Mark the article as read for the current user
        article.readers.add(request.user)

    # Render the article detail template with the retrieved article
    return render(request, 'blog/article_detail.html', {'article': article})
