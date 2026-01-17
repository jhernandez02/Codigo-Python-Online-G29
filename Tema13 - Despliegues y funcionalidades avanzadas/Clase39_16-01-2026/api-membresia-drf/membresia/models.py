from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Membresia(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Suscripcion(models.Model):
    membresia = models.ForeignKey(Membresia, on_delete=models.RESTRICT)
    usuario = models.ForeignKey(User, on_delete=models.RESTRICT)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    precio = models.FloatField()
    enlace_boleta = models.CharField(max_length=255, null=True)
    activo = models.CharField(max_length=1)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.fecha_inicio} {self.fecha_fin}"