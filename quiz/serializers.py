from rest_framework import serializers
from .models import Question, Quiz, Answer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'title', 'question', 'correct')

class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ('id', 'title', 'quiz', 'answer')

class QuizSerializer(serializers.ModelSerializer):
    quiz_questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Quiz
        fields = ('id', 'title', 'description', 'created_at', 'quiz_questions')


        