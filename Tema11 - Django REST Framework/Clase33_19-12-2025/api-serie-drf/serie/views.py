from rest_framework import viewsets, generics
from rest_framework.exceptions import NotFound
from .models import Categoria, Serie, Favorito
from .serializers import CategoriaSerializer, SerieSerializer, FavoritoSerializer

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

# ListAPIView retorna una lista de objetos
class FavoritoListView(generics.ListAPIView):
    serializer_class = FavoritoSerializer
    queryset = Favorito.objects.all()

class FavoritoUsuarioListView(generics.ListAPIView):
    serializer_class = FavoritoSerializer
    def get_queryset(self):
        usuarioId = self.kwargs['pk']
        return Favorito.objects.filter(usuario=usuarioId)

# RetrieveAPIView retorna solo un objeto
class FavoritoRetrieveView(generics.RetrieveAPIView):
    serializer_class = FavoritoSerializer
    queryset = Favorito.objects.all()

class FavoritoUsuarioRetrieveView(generics.RetrieveAPIView):
    serializer_class = FavoritoSerializer
    # get_object es el método que DRF usa para obtener un objecto exacto
    # que va a devolver una vista tipo Retrieve/Update/(Delete)
    def get_object(self):
        pk = self.kwargs['pk']
        iduser = self.kwargs['iduser']
        try:
            return Favorito.objects.get(pk=pk, usuario=iduser)
        except:
            raise NotFound()

class FavoritoUsuarioCreateView(generics.CreateAPIView):
    serializer_class = FavoritoSerializer
    queryset = Favorito.objects.all()

class FavoritoUsuarioDeleteView(generics.DestroyAPIView):
    serializer_class = FavoritoSerializer
    def get_object(self):
        pk = self.kwargs['pk']
        iduser = self.kwargs['iduser']
        try:
            return Favorito.objects.get(pk=pk, usuario=iduser)
        except:
            raise NotFound()

