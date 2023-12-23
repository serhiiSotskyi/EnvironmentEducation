from django import forms
from django.forms import inlineformset_factory
from .models import Quiz, Question, Answer  # Make sure to import Quiz

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['quiz_name']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'marks']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text', 'is_correct']

AnswerFormSet = inlineformset_factory(Question, Answer, form=AnswerForm, extra=2)
