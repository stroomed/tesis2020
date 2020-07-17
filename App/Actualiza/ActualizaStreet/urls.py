"""ActualizaStreet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import api
from .yasg import urlpatterns as doc_url


urlpatterns = [
    # Genera un esquema con un `request` válido a admin de django:
    path('admin/', admin.site.urls),
    # Genera un esquema con un `request` válido al login:
    path('', api.login, name = 'login'),
    # Genera un esquema con un `request` válido al historial:
    path('historial/',api.historial, name= 'historial'),
    # Genera un esquema con un `request` válido al registro:
    path('registro/',api.registro, name= 'registro'),
    path('informacion/',api.usuario, name= 'usuario'),
    path('edit/<int:id>',api.edit, name= 'Eusuario'),
    path('update/<int:id>',api.update, name= 'Uusuario'),
    path('del/<int:id>',api.destroy, name= 'Dusuario'),
    # Genera un esquema con un `request` válido al index de rest:
    path('api/', api.apiOverView, name='api-overview'),
    # Genera un esquema con un `request` válido a creacion de experimentos en rest:
    path('api/ex-create/', api.exCreate, name='ex-create'),
    path('api/ex-list/', api.exList, name='ex-list'),
    path('api/u-list/', api.uList, name='l-list'),
    path('/', api.LogOut, name='LogOut'),
    path("crear/",api.crear, name='crear'),
    path("imgcrear/",api.imgCrear, name="imgCreate"),
    path("vodcrear/",api.vodCrear, name="vodCreate"),
    path('api/img-create/', api.imgCreate, name='img-create'),
    path('api/img-list/', api.imgList, name='img-list'),
    path('api/vod-create/', api.vodCreate, name='vod-create'),
    path('api/vod-list/', api.vodList, name='vod-list'),
]

urlpatterns += doc_url