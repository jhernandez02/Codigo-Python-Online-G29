from rest_framework import serializers
from .models import Categoria, Serie, Favorito

# Los serializadores se encargna de convertir datos complejos (modelos)
# en formato JSON, y también toman datos enviados en formato JSON
# para convertirlos en objetos de Python

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombre', 'fecha_registro')

class SerieSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)
    class Meta:
        model = Serie
        fields = ('__all__')

class FavoritoSerializer(serializers.ModelSerializer):
    # Agregar el nombre del usuario, de la seria y de la categoría, a la lista
    # read_only define que el campo es de solo lectura, no lo soclita al crear o actualizar un registro
    usuario_nombre = serializers.CharField(source='usuario.username', read_only=True)
    serie_nombre = serializers.CharField(source='serie.nombre', read_only=True)
    categoria_nombre = serializers.CharField(source='serie.categoria.nombre', read_only=True)
    class Meta:
        model = Favorito
        fields = ('__all__')
        # La variable usuario no puede enviarse para ser asignado al campo usuario
        read_only_fields = ['usuario']
    
    def validate(self, data):
        # Obtenemos el id del usuario y de la serie enviados por el token
        idusuario = self.context['request'].user
        idserie = data['serie']
        # Verificamos si la serie ya existe en los favoritos del usuario
        if Favorito.objects.filter(usuario=idusuario,serie=idserie).exists():
            raise serializers.ValidationError("Esta serie ya se guardó como favorita")
        return data
