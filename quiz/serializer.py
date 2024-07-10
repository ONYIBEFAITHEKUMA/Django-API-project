from rest_framework.serializers import ModelSerializer
from.models import Quiz
from questions.Serializer import QuestionSerializer, OptionSerializer, AllQuestionSerializer
from questions.models import Question

class QuizSerializer(ModelSerializer):
    questions = AllQuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Quiz
        fields = '__all__'

class CreateQuizSerializer(ModelSerializer):
   
    class Meta:
        model = Quiz
        fields = [  'name', 'is_active', ' descriptions', ]
        
class UpdateQuizSerializer(ModelSerializer):
    class Meta:
        model = Quiz
        fields = [  'name', 'is_active', ]
        
