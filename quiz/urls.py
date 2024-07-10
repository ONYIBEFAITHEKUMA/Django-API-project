from django.urls import path
from . import views

urlpatterns = [
    path('status/', views.apiStatus, name='Status'),
    path('all', views.getAll, name='all'),
    path('create_Quiz', views.create_Quiz, name='create_quiz'),
    path('update_Quiz/<int:pk>',views.update_Quiz, name='update_Quiz'),
    path('delete_quiz/<int:pk>', views.delete_quiz, name='delete_quiz'),
]