from django.urls import path
from . import views

urlpatterns = [
    path('status/', views.apistatus, name='status'),
    path ('all', views.getALL, name='all' ),
    path('create', views.create, name='create'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
   
]