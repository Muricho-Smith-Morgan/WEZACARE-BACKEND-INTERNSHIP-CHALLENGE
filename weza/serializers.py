from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Question, Answer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {
            "password": {"write_only": True}
        }


class QuestionSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'body', 'author', 'created_at']


class AnswerSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = ['id', 'body', 'author', 'created_at']
