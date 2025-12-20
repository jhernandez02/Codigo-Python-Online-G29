from django.contrib import admin
from .models import Categoria, Serie, Favorito

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Serie)
admin.site.register(Favorito)