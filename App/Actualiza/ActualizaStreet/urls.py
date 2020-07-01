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
from api.api import UserAPI
from api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api.login, name = 'login'),
    path('base/',api.base, name = 'base'),
    path('historial/',api.historial, name= 'historial'),
    #path('registro/',api.UserRegister, name= 'registro'),
    path('api/1.0/create_user', UserAPI.as_view(), name = 'api_create_user'),
    path('api/', api.apiOverView, name='api-overview'),
    path('api/ex-list/', api.exList, name='ex-list'),
    path('api/ex-create/', api.exCreate, name='ex-create'),
]
