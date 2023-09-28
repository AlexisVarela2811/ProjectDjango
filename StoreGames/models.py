from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class UsuarioManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('El campo Email es obligatorio')
        usuario = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, username, email, password=None):
        usuario = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        usuario.is_superuser = True
        usuario.is_staff = True
        usuario.save(using=self._db)
        return usuario

    # Implementa el método get_by_natural_key
    def get_by_natural_key(self, username):
        return self.get(username=username)

class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=16, unique=True)
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    # Otros campos de tu modelo

    # Especifica aquí cuál es el campo que se utilizará como nombre de usuario
    USERNAME_FIELD = 'username'

    # Especifica aquí los campos que deben ser requeridos al crear un superusuario
    REQUIRED_FIELDS = ['email', 'nombre', 'apellidos']

    # Asigna el gestor personalizado a tu modelo
    objects = UsuarioManager()

    # Resto de campos y métodos de tu modelo
