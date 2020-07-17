from rest_framework.response import Response
from .serializers import ExperimentoSerializer, UsuarioSerializer, VideoSerializer, ImagenSerializer
from rest_framework import status
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from .models import experimento, imagen, video
from users.models import Usuario
from .forms import UsuarioForm, ExperimentoForm, ImagenForm, VideoForm
from django.contrib import messages
from django.contrib.sessions.models import Session

def registro(request):
    """
        Renderización del template 'register.html'
    """
    if request.session.has_key('is_logged_admin'):
        u_list = Usuario.objects.all()
        form = UsuarioForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('registro')
        return render(request, 'templates/register.html', {'form':form, 'list':u_list})
    return redirect('login')

def edit(request, id):
    if request.session.has_key('is_logged_admin'):
        user = Usuario.objects.get(idusuario=id)
        return render(request, 'templates/uEdit.html',{'user':user})
    return redirect('login')

def update(request, id):
    user = Usuario.objects.get(idusuario=id)
    form = UsuarioForm(request.POST, instance=user)
    if form.is_valid():
        form.save()
        return redirect('registro')
    return render(request, 'templates/uEdit.html', {'user':user})

def destroy(request, id):
    user = Usuario.objects.get(idusuario=id)
    user.delete()
    return redirect('registro')

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
            request.session['U_ape'] = u.apellido
            request.session['U_usu'] = u.usuario
            request.session['U_pass'] = u.contraseña
            request.session['U_mail'] = u.email
            request.session['U_fono'] = u.fono
            return redirect('historial')
        elif count2 > 0:
            request.session['is_logged_user'] = u.nombre
            request.session['U_ape'] = u.apellido
            request.session['U_usu'] = u.usuario
            request.session['U_pass'] = u.contraseña
            request.session['U_mail'] = u.email
            request.session['U_fono'] = u.fono
            return redirect('historial')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return redirect('login')
    return render(request, 'templates/login.html')

def LogOut(request):
    if  request.session.has_key('is_logged_admin'):
        del request.session['is_logged_admin']
        del request.session['U_ape']
        del request.session['U_usu']
        del request.session['U_pass']
        del request.session['U_mail']
        del request.session['U_fono']
        return redirect('login')
    elif request.session.has_key('is_logged_user'):
        del request.session['is_logged_user']
        del request.session['U_ape']
        del request.session['U_usu']
        del request.session['U_pass']
        del request.session['U_mail']
        del request.session['U_fono']
        return redirect('login')

def crear(request):
    if request.session.has_key('is_logged_admin') or request.session.has_key('is_logged_user'):
        form = ExperimentoForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('historial')
        return render(request, 'templates/ingreExp.html',{'form':form})
    return redirect('login')
 
def imgCrear(request):
    if request.session.has_key('is_logged_admin') or request.session.has_key('is_logged_user'):
        form = ImagenForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('historial')
        return render(request, 'templates/imgCreate.html', {'form':form})
    return redirect('login')

def vodCrear(request):
    if request.session.has_key('is_logged_admin') or request.session.has_key('is_logged_user'):
        form = VideoForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('historial')
        return render(request, 'templates/vodCreate.html', {'form':form})
    return redirect('login')

def historial(request):
    """
        Renderización del template 'historial.html'
        y un contexto de los objetos dentro de la tabla 'api_experimento'
        en la base de datos mongo
    """
    if request.session.has_key('is_logged_admin') or request.session.has_key('is_logged_user'):
        ex = experimento.objects.all()
        img = imagen.objects.all()
        vod = video.objects.all()
        return render(request, 'templates/historial.html',{'ex':ex,'img':img,'vod':vod})
    
    return redirect('login')

@api_view(['GET'])
def apiOverView(request):
    """
        Retorna una vista con las url's de la api
    """
    api_urls = {
        'Crear experimento':'api/ex-create/',
        'Lista de Experimentos':'api/ex-list/',
        'Crear Imagen':'api/img-create/',
        'Lista de Imagenes':'api/img-list/',
        'Listar Usuarios':'api/u-list/',
        'Crear Videos':'api/vod-create/',
        'Listar Videos':'api/vod-list/',
        
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

@api_view(['POST'])
def imgCreate(request):
    serializer = ImagenSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Creado exitosamente", status = status.HTTP_201_CREATED)
    else:
        return Response("Error al crear", status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def imgList(request):
    img = imagen.objects.all()
    serializer = ImagenSerializer(img, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def vodCreate(request):
    serializer = VideoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Creado exitosamente", status = status.HTTP_201_CREATED)
    else:
        return Response("Error al crear", status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def vodList(request):
    vod = video.objects.all()
    serializer = VideoSerializer(vod, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def uList(request):
    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def exList(request):
    expe = experimento.objects.all()
    serializer = ExperimentoSerializer(expe,many=True)
    return Response(serializer.data)