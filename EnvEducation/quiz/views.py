from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
import random

def quiz_list(request):
    # Retrieve all quizzes
    context = {"quizzes" : Quiz.objects.all(),}
    
    # Check if a specific quiz is selected and redirect to its detail page
    if request.GET.get('quiz'):
        return redirect(f"quiz_detail/?quiz={request.GET.get('quiz')}")
    
    return render(request, 'quiz/index.html', context)

def quiz_detail(request):
    # Get the quiz name from the request
    quiz_name = request.GET.get('quiz')
    
    # Get the quiz object or return a 404 error if not found
    quiz = get_object_or_404(Quiz, quiz_name=quiz_name)
    
    # Get the current user
    user = request.user

    # Mark the quiz as passed for the current user if authenticated
    if user.is_authenticated and quiz not in user.passed_quizzes.all():
        user.passed_quizzes.add(quiz)

    # Prepare context for rendering the quiz detail page
    context = {'quiz': quiz_name,
               'user': user}
    
    return render(request, 'quiz/quiz_detail.html', context)

def get_quiz(request):
    try:
        # Retrieve all questions or filter by quiz name if provided in the request
        question_objs = Question.objects.all()
        if request.GET.get('quiz'):
            question_objs = question_objs.filter(quiz__quiz_name__icontains=request.GET.get('quiz'))
        question_objs = list(question_objs)
        
        # Shuffle questions for randomness
        random.shuffle(question_objs)
        
        # Prepare JSON data for questions and answers
        data = []
        for question_obj in question_objs:
            data.append({
                "uid" : question_obj.uid,
                "quiz" : question_obj.quiz.quiz_name,
                "question" : question_obj.question,
                "marks" : question_obj.marks,
                "answers" : question_obj.get_answers()
            })
        
        # Create JSON response payload
        payload = {"status" : True, "data" : data}
        return JsonResponse(payload)
    except Exception as e:
        # Log any exceptions
        print(e)
    
    # Return a generic error response
    return HttpResponse("Something went wrong")
