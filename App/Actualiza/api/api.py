from rest_framework.response import Response
from .serializers import UserSerializer, ExperimentoSerializer
#from .serializers import PostForm
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.template import RequestContext
from .models import experimento


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
    ex = experimento.objects.all()
    return render(request,'templates/historial.html',{'ex':ex})

@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'Listas':'/ex-list/',
        'Crear':'/ex-create/',
    }
    return Response(api_urls)


@api_view(['POST'])
def exCreate(request):
    serializer = ExperimentoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)