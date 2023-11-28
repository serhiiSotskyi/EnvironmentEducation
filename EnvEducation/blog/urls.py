from django.urls import path
from . import views
from .views import article_list, article_detail

app_name = "blog"
urlpatterns = [
    path('', article_list, name='article_list'),
    path('article_detail/', article_detail, name='article_detail'),
    path('<int:article_id>/', article_detail, name='article_detail'),
]
