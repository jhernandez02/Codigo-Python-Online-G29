from rest_framework import viewsets, generics
from .models import Categoria, Serie
from .serializers import CategoriaSerializer, SerieSerializer

# El ModelViewSet es una clase de vista que proporciona
# un conjunto de operaciones (CRUD) para un modelo específico
class CategoriaViewSet(viewsets.ModelViewSet):
    # Definimos qué datos del modelo estarán disponibles
    # para ser consultados y modificados
    queryset = Categoria.objects.all().order_by('nombre')
    # Se especifica el serializador que se utilizará
    # para transformar los datos en el modelo Categoria
    # y los formatos de respuesta JSON
    serializer_class = CategoriaSerializer

class SerieViewSet(viewsets.ModelViewSet):
    queryset = Serie.objects.all().order_by('nombre')
    serializer_class = SerieSerializer

class SeriesPorCategoriaList(generics.ListAPIView):
    serializer_class = SerieSerializer
    # Definimos el queryset mediante la función get_queryset
    def get_queryset(self):
        categoriaId = self.kwargs['id']
        return Serie.objects.filter(categoria=categoriaId).order_by('nombre')