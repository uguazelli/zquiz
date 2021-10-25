from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    code = models.CharField(max_length=100)
    active = models.BooleanField()
    difficulty = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    question_number = models.IntegerField(null=True, blank=True)
    question_image = models.CharField(max_length=100, null=True, blank=True)
    question = models.TextField()
    answer = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.question_number)


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers"
    )
    answer = models.TextField(null=True, blank=True)
    answer_image = models.CharField(max_length=100, null=True, blank=True)
    is_correct = models.BooleanField(null=True)
    points = models.IntegerField(null=True, blank=True)


class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="results")
    points = models.IntegerField(null=True, blank=True)
    result = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.result
