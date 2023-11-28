from django.urls import path
from . import views
from .views import index, article_detail

app_name = "educationalMaterials"
urlpatterns = [
    path("", views.index, name="index"),
    path('<int:article_id>/', article_detail, name='article_detail'),
]