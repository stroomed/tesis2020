from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import render

class UserAPI(APIView):
    def post(self, request):
        serializer = UserSerializer( data = request.data )
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

def base(request):
    return render(request, 'templates/index.html')

def login(request):
    return render(request, 'templates/login.html')

def historial(request):
    return render(request, 'templates/historial.html')
    
def UserRegister(request):
    return render(request, 'templates/register.html')