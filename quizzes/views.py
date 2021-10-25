from django.http import response
from quizzes.mixin import MultipleFieldLookupMixin
from quizzes.models import Answer, Question, Quiz, Result
from quizzes.serializers import (
    AnswerSerializer,
    QuestionSerializer,
    QuizSerializer,
    ResultSerializer,
)
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class ListCreateQuestionQuiz(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


class RetrieveUpdateDestroyResultQuiz(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = QuizSerializer
    # queryset = Quiz.objects.filter(active=True)
    queryset = Quiz.objects.all()


class ListCreateQuestion(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class RetrieveUpdateDestroyResultQuestion(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = QuestionSerializer

    def get_queryset(self):
        quiz_id = self.kwargs["quiz_id"]
        return Question.objects.filter(quiz=quiz_id)


class ListCreateResult(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ResultSerializer
    queryset = Result.objects.all()


class RetrieveUpdateDestroyResult(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ResultSerializer

    def get_queryset(self):
        quiz_id = self.kwargs["quiz_id"]
        return Result.objects.filter(quiz=quiz_id)


class ListCreateAnswer(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()


class RetrieveUpdateDestroyAnswer(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = AnswerSerializer

    def get_queryset(self):
        quiz_id = self.kwargs["quiz_id"]
        question_id = self.kwargs["question_id"]
        quiz = Quiz.objects.get(pk=quiz_id)
        question = Question.objects.get(pk=question_id, quiz=quiz)
        return Answer.objects.filter(question=question)
