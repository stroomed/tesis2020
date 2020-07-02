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
