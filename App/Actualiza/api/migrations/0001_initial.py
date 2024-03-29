# Generated by Django 3.0.5 on 2020-07-17 02:20

from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='experimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experimento_id', models.IntegerField(null=True)),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.IntegerField(null=True)),
                ('longitud', models.FloatField(null=True)),
                ('latitud', models.FloatField(null=True)),
                ('fecha', models.DateTimeField()),
                ('señal', models.CharField(max_length=50, null=True)),
                ('estado', models.CharField(max_length=50, null=True)),
                ('experimento', djongo.models.fields.ArrayReferenceField(on_delete=django.db.models.deletion.CASCADE, to='api.experimento')),
            ],
        ),
        migrations.CreateModel(
            name='imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_id', models.IntegerField(null=True)),
                ('longitud', models.FloatField(null=True)),
                ('latitud', models.FloatField(null=True)),
                ('fecha', models.DateTimeField()),
                ('señal', models.CharField(max_length=50, null=True)),
                ('estado', models.CharField(max_length=50, null=True)),
                ('experimento', djongo.models.fields.ArrayReferenceField(on_delete=django.db.models.deletion.CASCADE, to='api.experimento')),
            ],
        ),
    ]
