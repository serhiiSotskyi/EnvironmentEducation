from django.urls import path
from . import views

app_name = "log"
urlpatterns = [
    # Path for user login
    path("logIn_user", views.logIn_user, name="logIn_user"),
    # Path for user signup
    path("signUp_user", views.signUp_user, name="signUp_user"),
    # Path for user logout
    path("logout_user", views.logout_user, name="logout_user"),
]
