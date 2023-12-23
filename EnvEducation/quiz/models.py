# models.py

from django.db import models
import uuid

class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Quiz(BaseModel):
    quiz_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.quiz_name
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        

class Question(BaseModel):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=100)
    marks = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.question_text

class Answer(BaseModel):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.answer_text
