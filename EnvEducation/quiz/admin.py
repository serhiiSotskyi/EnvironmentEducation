# admin.py

from django.contrib import admin
from django.template.loader import get_template
from django.forms import inlineformset_factory

from .models import Quiz, Question, Answer
from .forms import QuizForm, QuestionForm, AnswerForm

class AnswerInline(admin.StackedInline):
    model = Answer
    form = AnswerForm
    extra = 1

class QuestionInline(admin.StackedInline):
    model = Question
    form = QuestionForm
    inlines = [AnswerInline]
    extra = 1

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    form = QuizForm
    inlines = [QuestionInline]
