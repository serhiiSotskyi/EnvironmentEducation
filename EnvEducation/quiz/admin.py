from django.contrib import admin
from .models import *

# Define an inline admin for Answer model to be displayed within QuestionAdmin
class AnswerAdmin(admin.StackedInline):
    model = Answer

# Define QuestionAdmin to include AnswerAdmin as an inline
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]

# Register Quiz, QuestionAdmin, and Answer models with the Django admin
admin.site.register(Quiz)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
