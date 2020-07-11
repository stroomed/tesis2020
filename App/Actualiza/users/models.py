# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Roles(models.Model):
    idrol = models.AutoField(db_column='IdRol', primary_key=True)  # Field name made lowercase.
    rol = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'Roles'


class Usuario(models.Model):
    idusuario = models.AutoField(db_column='IdUsuario', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    fono = models.IntegerField()
    rol = models.ForeignKey(Roles, models.DO_NOTHING, db_column='rol')

    class Meta:
        managed = False
        db_table = 'Usuario'
