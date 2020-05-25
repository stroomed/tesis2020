from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from ActualizaStreet.actualiza.serializers import UserSerializer, GroupSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

def login(request):
    return render(request, 'login.html')

def administrator(request):
    return render(request, 'admin_index.html')

def mapa(request):
    return render(request, 'mapa.html')

def historial(request):
    return render(request, 'historial.html')