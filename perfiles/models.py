from django.db import models

# Create your models here.
class Perfiles(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    usuario=models.CharField(max_length=50, default="")
    contraseña=models.CharField(max_length=50)
    universidad=models.CharField(max_length=50)
    tipo=models.CharField(max_length=10)


class Candidatos(models.Model):
    titulo = models.CharField(max_length=255)
    salario = models.DecimalField(max_digits=10, decimal_places=2)


