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
    if request.session.has_key('is_logged_admin'):
        form = UsuarioForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'templates/register.html', {'form':form})
    return redirect('login')
    
def usuario(request):
    if request.session.has_key('is_logged_user'):
        return render(request,'templates/usuario.html')

def login(request):
    """
        Renderización del template 'login.html'
    """
    if request.POST:
        usuario = request.POST['user']
        contraseña = request.POST['pass']
        count1 = Usuario.objects.filter(usuario=usuario, contraseña=contraseña, rol=1).count()
        count2 = Usuario.objects.filter(usuario=usuario, contraseña=contraseña, rol=2).count()
        u = Usuario.objects.get(usuario=usuario)
        if count1 > 0:
            request.session['is_logged_admin'] = u.nombre
            return redirect('historial')
        elif count2 > 0:
            request.session['is_logged_user'] = u.nombre
            return redirect('historial')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return redirect('login')
    return render(request, 'templates/login.html')

def LogOut(request):
    if  request.session.has_key('is_logged_admin'):
        del request.session['is_logged_admin']
        return redirect('login')
    elif request.session.has_key('is_logged_user'):
        del request.session['is_logged_user']
        return redirect('login')

def historial(request):
    """
        Renderización del template 'historial.html'
        y un contexto de los objetos dentro de la tabla 'api_experimento'
        en la base de datos mongo
    """
    if request.session.has_key('is_logged_admin') or request.session.has_key('is_logged_user'):
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



