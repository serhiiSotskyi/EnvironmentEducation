from django.urls import path
from . import views
from .views import quiz_list

app_name = "quiz"
urlpatterns = [
    path("", views.quiz_list, name="quiz_list"),
    path("api/get-quiz/", views.get_quiz, name="get_quiz")
]

