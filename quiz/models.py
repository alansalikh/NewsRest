from django.db import models

# Create your models here.

class Quiz(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    title = models.CharField(max_length=255)
    quiz = models.ForeignKey(Quiz, related_name='quiz_questions', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Answer(models.Model):
    title = models.CharField(max_length=255)
    question = models.ForeignKey(Question, related_name='answer', on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.title

