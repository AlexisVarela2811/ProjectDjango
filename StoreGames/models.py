from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    correo = models.EmailField(unique=True)
    usuario = models.CharField(max_length=16, unique=True)
    contrasena = models.CharField(max_length=12)
    fechanacimiento = models.DateField()
    direccion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre
