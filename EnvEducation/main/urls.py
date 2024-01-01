from django.urls import path
from . import views
from .views import *

# Define the app namespace
app_name="main"
urlpatterns = [
    # Define the URL pattern for the root path and map it to the 'index' view
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
]
