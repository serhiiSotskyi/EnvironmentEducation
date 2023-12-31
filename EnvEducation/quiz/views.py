from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
import random
from django.views.decorators.http import require_POST
import json


def quiz_list(request):
    context = {"quizzes" : Quiz.objects.all(),}
    if request.GET.get('quiz'):
        return redirect(f"quiz_detail/?quiz={request.GET.get('quiz')}")
    return render(request, 'quiz/index.html', context)

def quiz_detail(request):
    quiz_name = request.GET.get('quiz')
    quiz = get_object_or_404(Quiz, quiz_name=quiz_name)
    user = request.user

    # Mark the quiz as passed for the current user
    if user.is_authenticated and quiz not in user.passed_quizzes.all():
        user.passed_quizzes.add(quiz)

    context = {'quiz': quiz_name,
               'user': user}
    return render(request, 'quiz/quiz_detail.html', context)

def get_quiz(request):
    try:
        question_objs = Question.objects.all()
        if request.GET.get('quiz'):
            question_objs = question_objs.filter(quiz__quiz_name__icontains=request.GET.get('quiz'))
        question_objs = list(question_objs)
        data = []
        random.shuffle(question_objs)
        for question_obj in question_objs:
            data.append({
                "uid" : question_obj.uid,
                "quiz" : question_obj.quiz.quiz_name,
                "question" : question_obj.question,
                "marks" : question_obj.marks,
                "answers" : question_obj.get_answers()
            })
        payload = {"status" : True, "data" : data}
        return JsonResponse(payload)
    except Exception as e:
        print(e)
    return HttpResponse("Something went wrong")
