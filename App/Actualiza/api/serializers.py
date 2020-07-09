from rest_framework import serializers
from django import forms
from .models import experimento
from django.contrib.auth.models import User


class ExperimentoSerializer(serializers.ModelSerializer):
    """
    toma el modelo y sus campos
    """
    class Meta:
        model = experimento
        fields = '__all__'