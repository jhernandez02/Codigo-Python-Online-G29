from rest_framework import serializers
from .models import Suscripcion

class SuscripcionSerializer(serializers.ModelSerializer):
    membresia_nombre = serializers.CharField(source='membresia.nombre', read_only=True)
    usuario_nombre = serializers.CharField(source='usuario.username', read_only=True)
    class Meta:
        model = Suscripcion
        fields = ('__all__')