from django.urls import path
from . import views

urlpatterns = [
    path('Status/', views.apiStatus, name='StatuS'),
]