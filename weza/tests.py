from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer, UserSerializer


class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data = {'username': 'testuser', 'password': 'testpass123'}
        response = self.client.post('/register/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')


class LoginTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', password='testpass123')

    def test_login(self):
        data = {'username': 'testuser', 'password': 'testpass123'}
        response = self.client.post('/login/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)


class QuestionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', password='testpass123')
        self.question = Question.objects.create(title='Test question', body='Test body', author=self.user)

    def test_get_questions_list(self):
        response = self.client.get('/questions/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_question_detail(self):
        response = self.client.get(f'/questions/{self.question.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.question.title)

    def test_create_question(self):
        self.client.force_authenticate(user=self.user)
        data = {'title': 'New question', 'body': 'New body'}
        response = self.client.post('/questions/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Question.objects.count(), 2)

    def test_create_question_unauthenticated(self):
        data = {'title': 'New question', 'body': 'New body'}
        response = self.client.post('/questions/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class AnswerTestCase(APITestCase):
    def setUp(self):
        self
