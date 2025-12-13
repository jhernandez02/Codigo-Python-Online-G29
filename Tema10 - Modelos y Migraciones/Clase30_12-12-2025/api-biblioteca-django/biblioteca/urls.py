from django.urls import path
from .views import genero, usuario, libro, prestamo

urlpatterns = [
    path('generos/', genero.listar),
    path('generos/crear', genero.crear),
    path('generos/mostrar/<int:id>', genero.mostrar),
    path('generos/editar/<int:id>', genero.editar),
    path('generos/eliminar/<int:id>', genero.eliminar),

    path('usuarios/', usuario.listar),
    path('usuarios/crear', usuario.crear),
    path('usuarios/mostrar/<int:id>', usuario.mostrar),
    path('usuarios/editar/<int:id>', usuario.editar),
    path('usuarios/eliminar/<int:id>', usuario.eliminar),

    path('libros/', libro.listar),
    path('libros/crear', libro.crear),
    path('libros/mostrar/<int:id>', libro.mostrar),
    path('libros/editar/<int:id>', libro.editar),
    path('libros/eliminar/<int:id>', libro.eliminar),

    path('prestamos/', prestamo.listar),
    path('prestamos/crear', prestamo.crear),
    path('prestamos/mostrar/<int:id>', prestamo.mostrar),
    path('prestamos/devolver/<int:id>', prestamo.devolver),
]