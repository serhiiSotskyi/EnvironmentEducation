from django.urls import path
from . import views

app_name = "log"
urlpatterns = [
    path("logIn_user", views.logIn_user, name="logIn_user"),
    path("signUp_user", views.signUp_user, name="signUp_user"),
    path("logout_user", views.logout_user, name="logout_user"),
]