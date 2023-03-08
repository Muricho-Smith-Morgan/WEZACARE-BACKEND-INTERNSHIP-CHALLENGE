from django.urls import path
from .views import QuestionList, QuestionDetail, AnswerCreate, AnswerUpdate, register, login

urlpatterns = [
path('register/', register, name='register'),
path('login/', login, name='login'),
path('questions/', QuestionList.as_view(), name='question_list'),
path('questions/int:pk/', QuestionDetail.as_view(), name='question_detail'),
path('questions/int:question_id/answers/', AnswerCreate.as_view(), name='answer_create'),
path('answers/int:pk/', AnswerUpdate.as_view(), name='answer_update'),
]