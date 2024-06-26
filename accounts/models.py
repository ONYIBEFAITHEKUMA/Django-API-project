from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# from quiz.models import UserQuizAttempt
from questions.models import Question, Options
from django.contrib.auth.hashers import make_password

# Create your models here.
class CustomUserManager(BaseUserManager):
   
    def create_user(self, username , email, password=None, **extra_fields ):
        if email is  None:
            raise TypeError('User must have an email address')
        if password is None:
            raise TypeError('enter ur password')
        
        user = self.model( username= username, email=self.normalize_email(email), **extra_fields)
        harshed_password = make_password(harshed_password)
        user.password = make_password
        user.save()
        return user
            
    def create_superUser(self, username , email, password=None, **extra_fields ):
        if email is None:
            raise TypeError('user email required')
        if password is  None:
            raise TypeError('user phone number required')
        
        user = self.create_superUser(email, password)
        user.is_createUser = True
        user.is_staff = True
        user.save()
        return user
       
    
class CustomUser(AbstractBaseUser):
    
    email = models.EmailField(unique=True)
    password = models.CharField()
    is_active = models.BooleanField
    is_staff =models.BooleanField
    created_at  = models.DateTimeField( auto_now_add=True)
    updated_at  = models.DateTimeField( auto_now_add=True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
    
    
    def __str__(self) :
        return self.email
    


class UserAnswer(models.Model):
    user = models.ForeignKey(CustomUser, related_name='user_answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    points  = models.FloatField()
    is_correct = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)
    
  

    def __str__(self):
        return f'{self.user} - {self.question} '