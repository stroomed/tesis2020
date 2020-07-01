from djongo import models
from django import forms
#Create your models here.

class video(models.Model):
    ubicacion = models.CharField(max_length=200,null=True)
    hora = models.DateField()
    señal = models.CharField(max_length=50,null=True)
    estado = models.CharField(max_length=50,null=True)
    class Meta:
        abstract = True
    

class imagen(models.Model):
    ubicacion = models.CharField(max_length=200,null=True)
    hora = models.DateField()
    señal = models.CharField(max_length=50,null=True)
    estado = models.CharField(max_length=50,null=True)
    class Meta:
        abstract = True

class experimento(models.Model):
    nombre = models.CharField(max_length=100,null=True)
    fecha = models.DateField()
    videos = models.EmbeddedField(
        model_container = video
    )
    imagenes = models.EmbeddedField(
        model_container = imagen
    )
    objects = models.DjongoManager()