from django.db import models

# Create your models here.

class Partido(models.Model):
    id = models.AutoField(primary_key=True)
    equipo_local = models.CharField(max_length=50)
    equipo_visitante=  models.CharField(max_length=50)
    goles_local = models.PositiveIntegerField()
    goles_visitante = models.PositiveIntegerField()
    jornada = models.PositiveIntegerField()


class Equipos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    año_fundacion = models.PositiveIntegerField
    estadio = models.CharField(max_length=50)
    aforo = models.PositiveIntegerField
    direccion = models.CharField(max_length=150)


class Jornada(models.Model):
    numero = models.PositiveIntegerField
    fecha = models.DateTimeField
    temporada = models.CharField(max_length=10)

class Temporada(models.Model):
    año = models.PositiveIntegerField