from rest_framework.response import Response
from .serializers import ExperimentoSerializer
from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import experimento

def registro(request):
    """
        Renderización del template 'register.html'
    """
    return render(request, 'templates/register.html')

def base(request):
    """
        Renderización del template 'index.html'
    """
    return render(request, 'templates/index.html')

def login(request):
    """
        Renderización del template 'login.html'
    """
    return render(request, 'templates/login.html')

def historial(request):
    """
        Renderización del template 'historial.html'
        y un contexto de los objetos dentro de la tabla 'api_experimento'
        en la base de datos mongo
    """
    ex = experimento.objects.all()
    return render(request,'templates/historial.html',{'ex':ex})

@api_view(['GET'])
def apiOverView(request):
    """
        Retorna una vista con las url's de la api
    """
    api_urls = {
        'Crear experimento':'/ex-create/',
        'Listar Usuarios':'/u-list/',
    }
    return Response(api_urls)




@api_view(['POST'])
def exCreate(request):
    """
        Crea experimentos en la base de datos `experimento`, valida y devuelve un mensaje
        
    """
    serializer = ExperimentoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Creado exitosamente", status = status.HTTP_201_CREATED)
    else:
        return Response("Error al crear", status = status.HTTP_400_BAD_REQUEST)


