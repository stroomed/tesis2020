from djongo import models
#Create your models here.

class experimento(models.Model):
    experimento_id = models.IntegerField(null=True)
    nombre = models.CharField(max_length=100,null=True)
    fecha = models.DateTimeField()

class video(models.Model):
    video_id = models.IntegerField(null=True)
    longitud = models.FloatField(null=True)
    latitud = models.FloatField(null=True)
    fecha = models.DateTimeField()
    señal = models.CharField(max_length=50,null=True)
    estado = models.CharField(max_length=50,null=True)
    experimento = models.ArrayReferenceField(
        to=experimento,
        on_delete = models.CASCADE,
    )
    objects = models.DjongoManager()
    

class imagen(models.Model):
    imagen_id = models.IntegerField(null=True)
    longitud = models.FloatField(null=True)
    latitud = models.FloatField(null=True)
    fecha = models.DateTimeField()
    señal = models.CharField(max_length=50,null=True)
    estado = models.CharField(max_length=50,null=True)
    experimento = models.ArrayReferenceField(
        to=experimento,
        on_delete = models.CASCADE,
    )
    objects = models.DjongoManager()



