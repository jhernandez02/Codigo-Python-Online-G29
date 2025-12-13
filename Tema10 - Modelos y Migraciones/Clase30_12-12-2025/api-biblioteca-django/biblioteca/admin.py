from django.contrib import admin
from .models import Genero, Usuario, Libro, Prestamo, PrestamoLibro

# Register your models here.

class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombres')
    search_fields = ('nombres',)

class LibroAdmin(admin.ModelAdmin):
    # Mostramos el campo nombre de genero
    list_display = ('id', 'isbn', 'titulo', 'genero__nombre', 'autor', 'disponibilidad')
    # Filtramos por el nombre de género
    list_filter = ('genero__nombre', 'disponible')
    search_fields = ('isbn', 'titulo', 'autor')

    def disponibilidad(self, obj):
        texto = True if obj.disponible=='1' else False
        return texto
    disponibilidad.boolean = True
    disponibilidad.short_description = 'Disponible'

class PrestamoLibroInline(admin.TabularInline):
    model = PrestamoLibro
    extra = 0 # Esto define cuantos formularios vacíos se mostrarán

    # Personalizamos los campos foreignkey que hay en el formulario
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'libro':
            # request.resolver_math es la ruta del admin actual
            # Si estamos creando, no hay object_id
            if 'object_id' not in request.resolver_match.kwargs:
                # Personalizamos la consulta para obtener solos los libros disponibles
                kwargs["queryset"] = Libro.objects.filter(disponible='1')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

class PrestamoAdmin(admin.ModelAdmin):
    # Mostramos el campo nombres de usuario
    list_display = ('id', 'usuario__nombres', 'fecha_registro', 'fecha_entrega', 'fecha_devolucion')
    # Busco por los nombres de los usuarios
    search_fields = ('usuario__nombres',)
    # Mostrar campos de solo lectura
    readonly_fields = ('fecha_registro',)
    # Añadimos el detalle como un inline
    inlines = [PrestamoLibroInline]

    # 1. save_model guarda el objeto principal en la base de datos
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        if obj.fecha_devolucion:
            for detalle in obj.detalles.all():
                libro = detalle.libro
                libro.disponible = '1'
                libro.save()
    
    # 2. save_related guarda los objetos relaciones: inlines
    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)

        prestamo = form.instance

        if not prestamo.fecha_devolucion:
            for detalle in prestamo.detalles.all():
                libro = detalle.libro
                libro.disponible = '0'
                libro.save()

admin.site.register(Genero, GeneroAdmin)
admin.site.register(Usuario, UserAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Prestamo, PrestamoAdmin)
