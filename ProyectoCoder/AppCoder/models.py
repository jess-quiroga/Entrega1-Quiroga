from xmlrpc.client import boolean
from django.db import models

# Create your models here.
class Actividades(models.Model):
    nombre=models.CharField(max_length=30)
    profesor= models.CharField(max_length=30)
    sede=models.CharField(max_length=30)


class Estudiantes(models.Model):
    nombre= models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    DNI=models.IntegerField()
    disciplina=models.CharField(max_length=30)


class Profesores(models.Model):
    nombre= models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    DNI=models.IntegerField()
    disciplina=models.CharField(max_length=30)


class Patrocinadores(models.Model):
    nombre= models.CharField(max_length=30)
    rubro=models.CharField(max_length=30)
    telefono=models.IntegerField()