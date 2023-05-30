from rest_framework import serializers

from .models import User, Question, Quiz


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields = ('username' , 'email', 'name', 'surname', 'isActive', 'registrationDate')
class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('text', 'author' , 'shuffleAnswer')

class QuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = ('questions', 'author')