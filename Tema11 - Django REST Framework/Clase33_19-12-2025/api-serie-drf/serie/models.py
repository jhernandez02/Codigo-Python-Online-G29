from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre

class Serie(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=150)
    fecha_lanzamiento = models.DateField()
    puntaje = models.IntegerField(default=0)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.RESTRICT)
    serie = models.ForeignKey(Serie, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.usuario.username} - {self.serie.nombre}"