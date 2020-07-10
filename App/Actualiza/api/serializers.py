from rest_framework import serializers
from django import forms
from .models import experimento
from users.models import Usuario


class ExperimentoSerializer(serializers.ModelSerializer):
    """
    toma el modelo y sus campos
    """
    class Meta:
        model = experimento
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = '__all__'