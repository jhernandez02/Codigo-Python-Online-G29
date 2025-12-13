from django.db import models

# Create your models here.
class Genero(models.Model):
    nombre = models.CharField(max_length=150)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombres = models.CharField(max_length=150)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombres

class Libro(models.Model):
    DISPONIBLE_LISTA = (
        ('0', 'No disponible'),
        ('1', 'Disponible'),
    )
    
    genero = models.ForeignKey(Genero, on_delete=models.RESTRICT, related_name='libros')
    isbn = models.CharField(max_length=25)
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    disponible = models.CharField(max_length=1, choices=DISPONIBLE_LISTA)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Prestamo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT, related_name='prestamos')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateField() # Fecha que se espera que el usuario devuelva los libros
    fecha_devolucion = models.DateField(blank=True, null=True) # Fecha cuando el usuario devuelve los libros

    def __str__(self):
        return 'Id: '+str(self.id)

class PrestamoLibro(models.Model):
    prestamo = models.ForeignKey(Prestamo, on_delete=models.RESTRICT, related_name='detalles')
    libro = models.ForeignKey(Libro, on_delete=models.RESTRICT)

    def __str__(self):
        return 'Id: '+str(self.id)
