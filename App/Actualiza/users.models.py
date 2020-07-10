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
    nrol = models.CharField(db_column='nRol', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Roles'


class Usuario(models.Model):
    idusuario = models.AutoField(db_column='IdUsuario', primary_key=True)  # Field name made lowercase.
    nusuario = models.CharField(db_column='nUsuario', max_length=50)  # Field name made lowercase.
    ausuario = models.CharField(db_column='aUsuario', max_length=50)  # Field name made lowercase.
    eusuario = models.CharField(db_column='eUsuario', max_length=100)  # Field name made lowercase.
    tusuario = models.IntegerField(db_column='tUsuario')  # Field name made lowercase.
    rusuario = models.ForeignKey(Roles, models.DO_NOTHING, db_column='rUsuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usuario'


class Validar(models.Model):
    usuario = models.OneToOneField(Usuario, models.DO_NOTHING, db_column='Usuario', primary_key=True)  # Field name made lowercase.
    contrasena = models.CharField(db_column='Contrasena', max_length=16)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Validar'
