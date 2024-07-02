from rest_framework.serializers import ModelSerializer
from .models import CustomUser

class customUserserializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'is_staff', 'created_at', 'updated_at']
        
class createcustomSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'first_name', 'last_name']
        
class updateCustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'first_name', 'last_name']
        
