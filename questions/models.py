from django.db import models
# from quiz.models import Quiz

# Create your models here.
class Question(models.Model):
    quiz = models.ForeignKey('quiz.Quiz',related_name='questions', on_delete=models.CASCADE )
    question  = models.CharField(max_length = 150)
    points = models.FloatField(default=1.5,  null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.question



class Options(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    A = models.CharField(max_length = 150, blank=True)
    B = models.CharField(max_length = 150, blank=True)
    C = models.CharField(max_length = 150, blank=True)
    D = models.CharField(max_length = 150, blank=True)
    Answer = models.CharField(choices=[('a' , 'a'), ('b', 'b'), ('c','c'), ('d', 'd')], max_length = 150)
   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.Answer
    