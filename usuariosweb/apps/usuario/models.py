from django.db import models

# Create your models here.
# Estructura de los datos
class usuarios(models.Model):
    usuario=models.CharField(max_length=50)
    nombrecompleto=models.CharField(max_length=80)
    correo=models.CharField(max_length=30)
    contraseña=models.CharField(max_length=30)
    documento=models.IntegerField()
    telefono=models.IntegerField()