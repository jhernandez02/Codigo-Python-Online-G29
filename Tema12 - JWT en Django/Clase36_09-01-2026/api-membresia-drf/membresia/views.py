from rest_framework import viewsets, generics
from .models import Suscripcion
from .serializers import SuscripcionSerializer

class SuscripcionViewSet(viewsets.ModelViewSet):
    queryset = Suscripcion.objects.all()
    serializer_class = SuscripcionSerializer
