from django.urls import path
from . import views

urlpatterns = [
   path('Status/', views.apiStatus, name='Status'),
   path('getAllquestion',views.getAllquestion, name='getAllquestion'),
   path('createQuestions', views.createQuestions, name='createQuestions'),
   path('updatequestion_Quiz/<int:pk>',views.updatequestion, name='updatequestion'),
   path('deletequestion/<int:pk>', views.deletequestion, name='deletequestion'),
   path('allOptions', views.getOptions, name='allOptions'),
   path('createOption', views.createOption, name='createOption'),
   path('all', views.getALL, name='all'),
   path('getAllOptions', views.getAllOptions, name='getAllOptions')
]
