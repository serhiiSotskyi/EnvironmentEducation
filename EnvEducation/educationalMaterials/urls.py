from django.urls import path
from . import views
from .views import *

app_name = "educationalMaterials"

urlpatterns = [
    path("", index, name="index"),  # URL pattern for the index page of educational materials
    path('<int:article_id>/', article_detail, name='article_detail'),  # URL pattern for viewing details of a specific article
]
