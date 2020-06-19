from django.db import models
#from mongoengine import *
#connect('default')
#Create your models here.
# class Experimento(EmbeddedDocument):
#     fecha = DateTimeField()
# class Señales(EmbeddedDocument):
#     experimento = ListField(EmbeddedDocumentField(Experimento))
#     ubicacion = StringField(max_length=100)
#     tipo_señal = StringField(max_length=100)
#     estado_señal = StringField(max_length=200)
#     hora = DateTimeField()
# class Historial(Document):
#     señales = ListField(EmbeddedDocumentField(Señales))