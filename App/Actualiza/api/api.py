from rest_framework.response import Response
from .serializers import ExperimentoSerializer, UsuarioSerializer
from rest_framework import status
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from .models import experimento
from users.models import Usuario
from .forms import UsuarioForm
from django.contrib import messages
from django.contrib.sessions.models import Session

def registro(request):
    """
        Renderización del template 'register.html'
    """
    if request.session.has_key('is_logged'):
        form = UsuarioForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'templates/register.html', {'form':form})
    return redirect('login')
    


def login(request):
    """
        Renderización del template 'login.html'
    """
    if request.POST:
        usuario = request.POST['user']
        contraseña = request.POST['pass']
        count = Usuario.objects.filter(usuario=usuario, contraseña=contraseña).count()
        if count > 0:
            request.session['is_logged'] = True
            return redirect('historial')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return redirect('login')
    return render(request, 'templates/login.html')

def LogOut(request):
    del request.session['is_logged']
    return redirect('login')

def historial(request):
    """
        Renderización del template 'historial.html'
        y un contexto de los objetos dentro de la tabla 'api_experimento'
        en la base de datos mongo
    """
    if request.session.has_key('is_logged'):
        ex = experimento.objects.all()
        return render(request, 'templates/historial.html',{'ex':ex})
    
    return redirect('login')

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



