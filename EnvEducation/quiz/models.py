from django.db import models
import uuid
import random
from django.contrib.auth.models import User

# Define a BaseModel with common fields for other models to inherit
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

# Model representing a Quiz
class Quiz(BaseModel):
    quiz_name = models.CharField(max_length=100)
    passed_by_users = models.ManyToManyField(User, blank=True, related_name='passed_quizzes')

    def __str__(self) -> str:
        return self.quiz_name
    
# Model representing a Question associated with a Quiz
class Question(BaseModel):
    quiz = models.ForeignKey(Quiz, related_name='question', on_delete=models.CASCADE)
    question = models.CharField(max_length=300)
    marks = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.question
    
    def get_answers(self):
        answer_objs = list(Answer.objects.filter(question=self))
        random.shuffle(answer_objs)
        data = []
        for answer_obj in answer_objs:
            data.append({
                "answer": answer_obj.answer,
                "is_correct": answer_obj.is_correct
            })
        return data

# Model representing an Answer associated with a Question
class Answer(BaseModel):
    question = models.ForeignKey(Question, related_name='answer', on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.answer

# Model representing a User's score in a specific Quiz
class UserQuizScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.quiz.quiz_name} - Score: {self.score}"
