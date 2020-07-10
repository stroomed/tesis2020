from rest_framework.response import Response
from .serializers import ExperimentoSerializer, UsuarioSerializer
from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import experimento
from users.models import Usuario
from .forms import UsuarioForm

def registro(request):
    """
        Renderización del template 'register.html'
    """
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        print('<h1>Creacion exitosa</h1>')
        form.save()
    
    return render(request, 'templates/register.html', {'form':form})
    


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
        'Crear experimento':'api/ex-create/',
        'Listar Usuarios':'api/u-list/',
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

@api_view(['GET'])
def uList(request):
    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)