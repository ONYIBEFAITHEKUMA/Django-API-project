from django.urls import path
from . import views


urlpatterns = [
    path('Status/', views.apiStatus, name='Status'),
    path('initiate_payment/', views.initiate_payment, name='initiate_payment'),
    path('verify/', views.verify, name='verify'),
    
]
