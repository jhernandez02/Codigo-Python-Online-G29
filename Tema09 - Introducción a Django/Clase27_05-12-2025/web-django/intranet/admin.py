from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Agenda, Proveedor

class AgendaAdmin(admin.ModelAdmin):
    # Definimos como mostramos la data en la tabla
    list_display = ('id', 'cliente', 'medio', 'fecha_formato', 'activo_icon', 'editar_icon', 'eliminar_icon')
    # Ordenamos por el campo fecha_agenda, de mayor a menor (-)
    ordering = ('-fecha_agenda',)

    class Media:
        css = {
            'all': ('admin_custom.css',)
        }

    # Personalizamos la fecha de la agenda
    def fecha_formato(self, obj):
        return obj.fecha_agenda.strftime('%d %b %Y  %H:%M')
    # Defiminos el titulo de la cabecera para la fecha
    fecha_formato.short_description = 'Fecha Agenda'

    def activo_icon(self, obj):
        activo_value = '✅' if obj.activo=='1' else '❌'
        return format_html(activo_value)
    activo_icon.short_description = 'Activo'

    # Definimos el botón para la acción de editar
    def editar_icon(self, obj):
        view_name = "admin:{}_{}_change".format(obj._meta.app_label, obj._meta.model_name)
        url = reverse(view_name, args=[obj.id])
        return format_html('<a href="{}">✏</a>', url)
    editar_icon.short_description = 'Editar'

    # Definimos el botón para la acción de eliminar
    def eliminar_icon(self, obj):
        view_name = 'admin:intranet_agenda_delete'
        url = reverse(view_name, args=[obj.id])
        return format_html('<a href="{}">🗑</a>', url)
    eliminar_icon.short_description = 'Eliminar'

class ProveedorAdmin(admin.ModelAdmin):
    # Definimos como mostramos la data en la tabla
    list_display = ('id', 'nombre', 'servicio', 'contacto_nombre', 'contacto_telefono', 'activo_icon')
    # Ordenamos por el campo nombre
    ordering = ('nombre',)
    # Agregamos los filtros
    list_filter = ('servicio','activo')
    # Agregamos los campos de búsqueda
    search_fields = ('nombre','contacto_nombre')
    # Agregamos más funciones de acción
    actions = ('make_agenda_available',)

    class Media:
        css = {
            'all': ('admin_custom.css',)
        }

    def make_agenda_available(self, request, queryset):
        queryset.update(activo='1')
    make_agenda_available.short_description = 'Habilitar proveedores seleccionados'

    def activo_icon(self, obj):
        activo_value = True if obj.activo=='1' else False
        return activo_value
    activo_icon.boolean = True
    activo_icon.short_description = 'Activo'


# Register your models here.
admin.site.register(Agenda, AgendaAdmin)
admin.site.register(Proveedor, ProveedorAdmin)