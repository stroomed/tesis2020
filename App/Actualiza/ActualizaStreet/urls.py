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
    # Genera un esquema con un `request` válido al index de rest:
    path('api/', api.apiOverView, name='api-overview'),
    # Genera un esquema con un `request` válido a creacion de experimentos en rest:
    path('api/ex-create/', api.exCreate, name='ex-create'),

    path('api/u-list/', api.uList, name='l-list'),
]

urlpatterns += doc_url