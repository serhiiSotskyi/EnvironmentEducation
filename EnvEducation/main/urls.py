from django.urls import path
from . import views
from .views import *

app_name="main"
urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path('submit_form/', submit_form, name='submit_form'),
]
