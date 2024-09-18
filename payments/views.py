from django.shortcuts import render
from rest_framework import status

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import CustomUser
from .models import paymentmethod
from rest_framework.permissions import AllowAny, IsAuthenticated
import requests
from django.conf import settings
import json
import random


@api_view(['GET'])
def apiStatus(request):
    return Response({'status': 'payment API is working'}, status=status.HTTP_200_OK)

def generat_trnx_ref():
    rand_num = ''
    for i in range(10):
        rand_num += str(random.randint(0, 9))
    trnx_ref = 'TRNX-' + rand_num
    return trnx_ref
    

@api_view(['POST'])
@permission_classes([AllowAny])
def initiate_payment(request):
    try:
        if request.method == 'POST':
            amount = request.POST.get('amount')
            trnx_ref = generat_trnx_ref()
            user_id = request.POST.get('user_id')
            email = request.POST.get('email')
            url = 'https://api.flutterwave.com/v3/payments'
            headers = {
                "Content-Type": 'application/json',
                'Authorization': f"Bearer {settings.FLUTTERWAVE_SECRET_KEY}",
               
            }
            data = {
                 'tx_ref': trnx_ref,
                "amount": amount,
                "currency": 'NGN',
                "redirect_url": request.build_absolute_uri('/payments/verify/'),
                
                "customer" : {
                    "email": email,
                    "phonenumber": '08027106648',
                    "name": email,
                },
                "customizations": {
                    "title": 'payment for Quiz',
                    "discription": 'Payment before writing a quize',
                    "Logo": "https://assets.piedpiper.com/logo.png",
                },
                "meta": {
                    "user_id": user_id,
                }
                
            }
            
            print(data['redirect_url'])
            response = requests.post(url, headers=headers, data=json.dumps(data))
            response_data = response.json()
            return Response(response_data, status=status.HTTP_200_OK)
        return Response({'error': 'invalid request'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': f'{e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
@api_view(['GET'])
def verify(request):
    try:
        tx_ref = request.GET.get('tx_ref')
        tx_status = request.GET.get('Status')
        tranx_id = request.GET.get('transaction_id')
        
        url =  f"https://api.flutterwave.com/v3/transactions/{tranx_id}/verify"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f"Bearer  {settings.FLUTTERWAVE_SECRET_KEY}",
            
            }
        response = requests.get(url, headers=headers)
        print(response)
        if response.status == 'success':
            print(response.data)
        else:
            print(response.message)
    except Exception as e:
        
        return Response({'error': f"{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        

