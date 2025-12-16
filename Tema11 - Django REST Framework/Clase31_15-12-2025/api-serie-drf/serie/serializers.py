from rest_framework import serializers
from .models import Categoria, Serie

# Los serializadores se encargna de convertir datos complejos (modelos)
# en formato JSON, y también toman datos enviados en formato JSON
# para convertirlos en objetos de Python

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombre', 'fecha_registro')

class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = ('__all__')