from django.urls import path
from . import views

app_name = "legal"
urlpatterns = [
    path("privacy_policy", views.privacyPolicy, name="privacy_policy"),
    path("terms_of_use", views.termsOfUse, name="terms_of_use")
]