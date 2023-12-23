from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import *
import random

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/index.html', {'quizzes' : quizzes})

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    return render(request, "quiz/quiz_detail.html", {'quiz' : quiz})

def get_quiz(request):
    try:
        question_objs = list(Question.objects.all())
        data = []
        random.shuffle(question_objs)
        for question_obj in question_objs:
            data.append({
                'quiz' : question_obj.quiz.quiz_name,
                'question' : question_obj.question,
                'marks' : question_obj.marks,
                'answers' : question_obj.get_answers()
            })

        payload = {'status' : True, 'data' : data}
        return JsonResponse(payload)

    except Exception as e:
        print(e)
    return HttpResponse("Something went wrong")