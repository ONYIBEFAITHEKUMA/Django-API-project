from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Question, Options
# from rest_framework.permissions import AllowAny
from . Serializer import QuestionSerializer, CreateQuestionSerializer, UpdateQuestionSerializer, OptionSerializer,CreateOptionsSerailizer, AllQuestionSerializer
from accounts.pagination import CustomPagination

# Create your views here.
@api_view(['GET'])

def apiStatus(request):
    return Response({'status': 'Question API is working'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def getAllquestion(request):
    question = Question.objects.all().order_by('created_at')
    pagination = CustomPagination()  
    pagination_question = pagination.paginate_queryset(question, request)
    serializer = QuestionSerializer(pagination_question, many=True)
    return pagination.get_paginated_response(serializer.data)

@api_view(['POST'])
def createQuestions(requset):
    serializer = CreateQuestionSerializer(data=requset.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updatequestion(request, pk):
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return Response({'error': 'question does not exist'}, status=status.HTTP_404_NOT_FOUND)
    serializer = UpdateQuestionSerializer(question, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deletequestion(request, pk):
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return Response({'error': 'question does not exist'}, status=status.HTTP_404_NOT_FOUND)
    question.delete()
    return Response({'message': 'question deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def getAllOptions(request):
    options = Options.objects.all().order_by('created_at')
    pagination = CustomPagination()
    pagination_option = pagination.paginate_queryset(options, request)
    serializer = OptionSerializer(pagination_option, many= True)
    return pagination.get_paginated_response(serializer.data)
     
@api_view(['GET'])
def getOptions(request):
    try:
        options = Options.objects.all().order_by('created_at')
        serializer = OptionSerializer(options, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Options.DoesNotExist:
        return Response({'error': 'this option does not exist'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def createOption(request):
    serializer = CreateOptionsSerailizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getALL(request):
    question_option = Question.objects.all().order_by('created_at').prefetch_related('options')
    serializer = AllQuestionSerializer(question_option, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)








