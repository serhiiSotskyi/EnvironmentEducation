from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.index, name="index"),
    path("article1", views.article1, name="article1"),
    path("article2", views.article2, name="article2"),
    path("article3", views.article3, name="article3"),
]