from django.urls import path
from .views import QuizListView, QuizDetailView, QuizQuestionView, QuizQuestion1View

urlpatterns = [
    path('quiz/', QuizListView.as_view(), name='all_quiz'),
    path('quiz/<int:pk>/', QuizDetailView.as_view(), name='quiz'),
    path('quiz/<int:quiz_id>/question/1/', QuizQuestion1View.as_view(), name='question_1'),
    path('quiz/<int:quiz_id>/question/<int:number>/<int:idenef>/', QuizQuestionView.as_view(), name='question'),
]
