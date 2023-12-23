# quiz_app/views.py
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
import random
from django.core.serializers import serialize

def quiz_list(request):
    questions = Question.objects.all()
    return render(request, 'quiz/index.html', {'questions': questions})

def get_quiz(request):
    try:
        question_objs = list(Question.objects.all())
        data = []
        random.shuffle(question_objs)
        for question_obj in question_objs:
            data.append({
                'category' : question_obj.category.category_name,
                'question' : question_obj.question,
                'marks' : question_obj.marks,
                'answers' : question_obj.get_answers()
            })

        payload = {'status' : True, 'data' : data}
        return JsonResponse(payload)

    except Exception as e:
        print(e)
    return HttpResponse("Something went wrong")
    
