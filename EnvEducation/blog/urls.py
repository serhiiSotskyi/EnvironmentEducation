from django.urls import path
from . import views
from .views import article_list, article_detail

# Namespace for the 'blog' app
app_name = "blog"

# URL patterns for the 'blog' app
urlpatterns = [
    # Path to view the list of articles
    path('', article_list, name='article_list'),

    # Path to view the details of a specific article identified by its ID
    path('<int:article_id>/', article_detail, name='article_detail'),
]
