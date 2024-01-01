from django.urls import path
from . import views

# Define the app_name for namespacing the URLs
app_name = 'creativeTask'

urlpatterns = [
    # Define the URL pattern for the index view
    path('', views.index, name='index'),
]
