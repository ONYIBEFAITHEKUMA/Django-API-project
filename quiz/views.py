from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import QuizSerializer,CreateQuizSerializer, UpdateQuizSerializer
from .models import Quiz

# Create your views here.
@api_view(['GET'])
def apiStatus(request):
    return Response({'status': 'Quiz API is working'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getAll(requst):
    quizzes = Quiz.objects.all().order_by('created_at').prefetch_related('questions')
    serializer = QuizSerializer(quizzes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_Quiz(request):
    serializer = QuizSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_Quiz(requst, pk):
    try:
        quiz = Quiz.objects.get(pk=pk)
    except Quiz.DoesNotExist:
        return Response({'error': 'this quiz does not exist'}, status=status.HTTP_404_NOT_FOUND)
    serializer = UpdateQuizSerializer(quiz, data=requst.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def delete_quiz(request, pk):
    try:
        quiz = Quiz.objects.get(pk=pk)
    except Quiz.DoesNotExist:
        return Response({'erro':'quiz does not exist'}, status=status.HTTP_404_NOT_FOUND)
    quiz.delete()
    return Response({'message': 'quiz deleted successfully'}, status=status.HTTP_204_NO_CONTENT)








