from django.urls import path
from . import views
from .views import *

app_name = "quiz"
urlpatterns = [
    path("", quiz_list, name="quiz_list"), # Path for the main quiz list view
    path("api/get-quiz/", get_quiz, name="get_quiz"), # API endpoint to get quiz details
    path("quiz_detail/", quiz_detail, name="quiz_detail"), # Path for the quiz detail view
]

