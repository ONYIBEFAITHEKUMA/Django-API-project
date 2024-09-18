from rest_framework.serializers import ModelSerializer
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class customUserserializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        
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
        
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        token['username'] = user.username
        token['email'] = user.email
        # token['is_active'] = user.is_active
        # token['is_staff'] = user.is_staff
        
        
        return token