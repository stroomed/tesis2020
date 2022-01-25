# Generated by Django 3.0.5 on 2020-07-11 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('idrol', models.AutoField(db_column='IdRol', primary_key=True, serialize=False)),
                ('rol', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Roles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idusuario', models.AutoField(db_column='IdUsuario', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=50)),
                ('usuario', models.CharField(max_length=50)),
                ('contraseña', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=100)),
                ('fono', models.IntegerField()),
            ],
            options={
                'db_table': 'Usuario',
                'managed': False,
            },
        ),
    ]