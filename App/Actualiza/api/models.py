from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField
#Create your models here.

class video(models.Model):
    ubicacion = models.CharField(max_length=200)
    hora = models.datetimeField()
    señal = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

class imagen(models.Model):
    ubicacion = models.CharField(max_length=200)
    hora = models.datetimeField()
    señal = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

class experimento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    solicitud = ListField(EmbeddedModelField('video','imagen'))