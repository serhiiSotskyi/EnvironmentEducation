from django.urls import path
from . import views

app_name = "educationalMaterials"
urlpatterns = [
    path("", views.index, name="index"),
    path("page1", views.page1, name="page1")
]