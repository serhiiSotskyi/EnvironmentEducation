from django.urls import path
from . import views

app_name = "log"
urlpatterns = [
    path("logIn", views.logIn, name="logIn"),
    path("signUp", views.signUp, name="signUp")
]