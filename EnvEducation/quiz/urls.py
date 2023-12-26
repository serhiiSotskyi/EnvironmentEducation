from django.urls import path
from . import views
from .views import *

app_name = "quiz"
urlpatterns = [
    path("", quiz_list, name="quiz_list"),
    path("api/get-quiz/", get_quiz, name="get_quiz"),
    path("quiz_detail/", quiz_detail, name="quiz_detail")
]

