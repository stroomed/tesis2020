from rest_framework import serializers
from django import forms
from django.contrib.auth.models import User
from .models import experimento
#from django.contrib.auth.models import Experiment, Signals, History

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = usuarios
#         fields = {'nUsuario','aUsuario','eUsuario','tUsuario','rUsuario'}

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()

    def create(self, validate_data):
        instance = User()
        instance.first_name = validate_data.get('first_name')
        instance.last_name = validate_data.get('last_name')
        instance.username = validate_data.get('username')
        instance.email = validate_data.get('email')
        instance.set_password(validate_data.get('password'))
        instance.save()
        return instance
    
    def validate_username(self, data):
        users = User.objects.filter(username = data)
        if len(users) != 0:
            raise serializers.ValidationError("Este nombre de usuario ya existe, ingrese uno nuevo")
        else:
            return data

class ExperimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = experimento
        fields = '__all__'
    
    


#class GetExperiment(serializers.Serializer):
#    id = serializers.ReadOnlyField()
#    fecha = serializers.CharField()
#
#    def createE(self, validate_data):
#        instanceE = Experiment()
#        instanceE.fecha = validate_data.get('fecha')
#        instanceE.save()
#        return instanceE
#    
#class Singals(serializers.Serilizer):
#    id = serializers.ReadOnlyField()
#    experimento = ¿?
#    ubicacion = serializers.CharField()
#    tipo_señal = serializers.CharField()
#    señal_estado = serializers.CharField()
#    hora = serializers.CharField()
#
#    def createS(self, validate_data):
#        instanceS = Signals()
#        instanceS.experimento = validate_data.get('experimento?') 
#        instanceS.ubicacion = validate_data.get('ubicacion') 
#        instanceS.tipo_señal = validate_data.get('tipo_señal') 
#        instanceS.señal_estado = validate_data.get('señal_estado') 
#        instanceS.hora = validate_data.get('hora')
#        instanceS.save()
#        return instanceS 
#
#class History(serializers.Serilizer):
#    id = serializers.ReadOnlyField()
#    experimento = ¿?
#    señales_detectadas = ¿?
#    
#    def createH(self, validate_data):
#       instanceH = History()
#       instanceH.experimento = validate_data.get('experimento?')
#       instanceH.señales_detectadas = validate_data.get('señales_detectadas?')
#       instanceH.save()
#       return instanceH