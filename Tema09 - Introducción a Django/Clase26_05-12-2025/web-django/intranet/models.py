from django.db import models
from django.utils import timezone

ACTIVO_LISTA = (
    ('1','Activo'),
    ('0','Inactivo'),
)

# Create your models here.
class Agenda(models.Model):

    MEDIO_LISTA = (
        ('L','Llamada'),
        ('V','Videollamada'),
        ('P', 'Presencial'),
        ('C', 'Correo')
    )

    cliente = models.CharField(max_length=150)
    medio = models.CharField(max_length=25, choices=MEDIO_LISTA)
    descripcion = models.TextField(null=True)
    fecha_agenda = models.DateTimeField()
    activo = models.CharField(max_length=1, default='1', choices=ACTIVO_LISTA)
    fecha_registro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.cliente

class Proveedor(models.Model):

    SERVICIO_LISTA = (
        ('Marketing y ventas', 'Marketing y ventas'),
        ('Tecnología', 'Tecnología'),
        ('Finaciero', 'Finaciero'),
        ('Operativo y Logística', 'Operativo y Logística'),
        ('Mantenimiento y Postventa', 'Mantenimiento y Postventa'),
    )

    CARGO_LISTA = (
        ('Jefe de Sucursal', 'Jefe de Sucursal'),
        ('Jefe de Taller', 'Jefe de Taller'),
        ('Jefe de Compras', 'Jefe de Compras'),
        ('Asistente de Compras', 'Asistente de Compras'),
        ('Asesor de Servicio', 'Asesor de Servicio'),
    )

    nombre = models.CharField(max_length=100)
    servicio = models.CharField(max_length=100, choices=SERVICIO_LISTA)
    direccion = models.CharField(max_length=150)
    contacto_nombre = models.CharField(max_length=150)
    contacto_telefono = models.CharField(max_length=25)
    contacto_cargo = models.CharField(max_length=45, choices=CARGO_LISTA)
    activo = models.CharField(max_length=1, default='1', choices=ACTIVO_LISTA)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
