from rest_framework.serializers import ModelSerializer
from .models import Question, Options


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'quiz', 'question', 'created_at', 'updated_at']

class CreateQuestionSerializer(ModelSerializer):
     class Meta:
        model = Question
        fields = [ 'quiz', 'question', ]
        

class UpdateQuestionSerializer(ModelSerializer):
     class Meta:
        model = Question
        fields = ['quiz', 'question', ]


class OptionSerializer(ModelSerializer):
    class Meta:
        model = Options
        exclude  = ['Answer',]
        
class CreateOptionsSerailizer(ModelSerializer):
    class Meta:
        model = Options
        fields = '__all__'
        
class AllQuestionSerializer(ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = '__all__'