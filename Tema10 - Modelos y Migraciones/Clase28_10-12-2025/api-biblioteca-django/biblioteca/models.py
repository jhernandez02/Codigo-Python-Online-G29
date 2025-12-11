from django.db import models

# Create your models here.
class Genero(models.Model):
    nombre = models.CharField(max_length=150)
    fecha_registro = models.DateTimeField(auto_now_add=True)

class Usuario(models.Model):
    nombres = models.CharField(max_length=150)
    fecha_registro = models.DateTimeField(auto_now_add=True)

class Libro(models.Model):
    genero = models.ForeignKey(Genero, on_delete=models.RESTRICT, related_name='libros')
    isbn = models.CharField(max_length=25)
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    disponible = models.CharField(max_length=1)
    fecha_registro = models.DateTimeField(auto_now_add=True)

class Prestamo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT, related_name='prestamos')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateField()
    fecha_devolucion = models.DateField(null=True)

class PrestamoLibro(models.Model):
    prestamo = models.ForeignKey(Prestamo, on_delete=models.RESTRICT, related_name='detalles')
    libro = models.ForeignKey(Libro, on_delete=models.RESTRICT)

