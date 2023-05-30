from django.db import models

# Create your models here.

#user
class User(models.Model):
    username = models.CharField(max_length=250, blank=False, null=False)
    email = models.EmailField()
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    passw = models.CharField(max_length=250)
    isActive = models.BooleanField(default=True)
    registrationDate = models.DateTimeField(auto_now_add=True, blank=True)
class Question(models.Model):
    text = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    shuffleAnswer = models.BooleanField(default=True)

class Answer(models.Model):
    text = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
class QuestionAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    answerOrder = models.IntegerField(default=1)
    IsCorrect = models.BooleanField(default=False)
class Quiz(models.Model):
    class Meta:
        verbose_name_plural = "Quizes"

    questions = models.ManyToManyField(Question)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)




