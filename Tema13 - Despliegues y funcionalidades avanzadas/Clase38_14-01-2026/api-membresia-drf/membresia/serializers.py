from rest_framework import serializers
from .models import Suscripcion

class SuscripcionSerializer(serializers.ModelSerializer):
    membresia_nombre = serializers.CharField(source='membresia.nombre', read_only=True)
    usuario_nombre = serializers.CharField(source='usuario.username', read_only=True)
    class Meta:
        model = Suscripcion
        fields = ('__all__')
        read_only_fields = ['usuario']

class BoletaItemSerializer(serializers.Serializer):
    descripcion = serializers.CharField(required=True)
    cantidad = serializers.IntegerField(required=True, min_value=1)
    valor_unitario = serializers.DecimalField(required=True,max_digits=10,decimal_places=2)

class BoletaSerializer(serializers.Serializer):
    operacion = serializers.CharField(required=True)
    tipo_de_comprobante = serializers.IntegerField(required=True)
    serie = serializers.CharField(required=True)
    numero = serializers.IntegerField(required=True)
    cliente_numero_de_documento = serializers.CharField(required=True)
    cliente_denominacion = serializers.CharField(required=True)
    items = BoletaItemSerializer(many=True)

