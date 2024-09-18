from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import CustomUser
from . Serializer import customUserserializer, createcustomSerializer, updateCustomUserSerializer, CustomTokenObtainPairSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth.hashers import make_password

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    view = TokenObtainPairView.as_view(serializer_class = CustomTokenObtainPairSerializer)
    return view(request._request)
    
    
@api_view(['POST'])
@permission_classes([AllowAny])
def refresh(request):
   view = TokenRefreshView.as_view()
   return view(request._request)

@api_view(['GET'])
def apistatus(request):
    return Response({'status': 'Account API is working'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def getALL(request):
    users = CustomUser.objects.all().order_by('created_at')
    serializer = customUserserializer(users, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def create(request):
    serializer = createcustomSerializer(data=request.data)
    if serializer.is_valid():
        password = serializer.validated_data['password']
        harshed_password = make_password(password)
        serializer.validated_data['password'] = harshed_password
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update(request, pk):
    try:
        user = CustomUser.objects.get(pk=pk)
    except CustomUser.DoesNotExist:
        return Response({'erro': 'User does not exit'}, status=status.HTTP_404_NOT_FOUND)
    serializer = updateCustomUserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete(request, pk):
    try:
        user = CustomUser.objects.get(pk=pk)
    except CustomUser.DoesNotExist:
        return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
    user.delete()
    return Response({'Message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)