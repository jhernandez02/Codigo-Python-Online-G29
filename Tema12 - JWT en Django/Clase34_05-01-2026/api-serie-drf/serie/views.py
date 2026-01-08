from rest_framework import viewsets, generics
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated, AllowAny
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

    def get_permissions(self):
        if self.action=='list' or self.action=='retrieve':
            return [AllowAny()]
        else:
            return [IsAuthenticated()]

class SeriesPorCategoriaList(generics.ListAPIView):
    serializer_class = SerieSerializer
    permission_classes = [AllowAny]
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
        # Filtramos solo los registros del usuario que ha solicitado la petición
        return Favorito.objects.filter(usuario=self.request.user)

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
        try:
            # Filtramos solo el registro, con el usuario que ha solicitado la petición
            return Favorito.objects.get(pk=pk, usuario=self.request.user)
        except:
            raise NotFound()

class FavoritoUsuarioCreateView(generics.CreateAPIView):
    serializer_class = FavoritoSerializer
    queryset = Favorito.objects.all()

    # perform_create se ejecuta justo despues que los datos han sido validados y antes de enviar  la respuesta
    def perform_create(self, serializer):
        # Asignamos el valor del campo usuario
        serializer.save(usuario=self.request.user)

class FavoritoUsuarioDeleteView(generics.DestroyAPIView):
    serializer_class = FavoritoSerializer

    def get_object(self):
        pk = self.kwargs['pk']
        print(pk, self.request.user)
        try:
            # Validamos que solo se elimine el registro que le pertenece al usuario que solicito
            return Favorito.objects.get(pk=pk, usuario=self.request.user)
        except:
            raise NotFound()

