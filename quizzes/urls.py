from django.urls import path

from . import views

urlpatterns = [
    path("", views.ListCreateQuestionQuiz.as_view(), name="ListCreateQuestionQuiz"),
    path(
        "<int:pk>/",
        views.RetrieveUpdateDestroyResultQuiz.as_view(),
        name="RetrieveUpdateDestroyResultQuiz",
    ),
    path(
        "<int:pk>/question/",
        views.ListCreateQuestion.as_view(),
        name="ListCreateQuestion",
    ),
    path(
        "<int:quiz_id>/question/<int:pk>/",
        views.RetrieveUpdateDestroyResultQuestion.as_view(),
        name="RetrieveUpdateDestroyResultQuestion",
    ),
    path(
        "<int:quiz_id>/question/<int:question_id>/answer/",
        views.ListCreateAnswer.as_view(),
        name="ListCreateAnswer",
    ),
    path(
        "<int:quiz_id>/question/<int:question_id>/answer/<int:pk>",
        views.RetrieveUpdateDestroyAnswer.as_view(),
        name="RetrieveUpdateDestroyAnswer",
    ),
    path("<int:pk>/result/", views.ListCreateResult.as_view(), name="ListCreateResult"),
    path(
        "<int:quiz_id>/result/<int:pk>/",
        views.RetrieveUpdateDestroyResult.as_view(),
        name="RetrieveUpdateDestroyResult",
    ),
]
