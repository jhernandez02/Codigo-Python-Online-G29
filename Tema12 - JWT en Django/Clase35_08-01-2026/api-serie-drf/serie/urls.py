from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'series', views.SerieViewSet)

urlpatterns = [
    # locahost:8000/api/v1/categorias           [GET, POST]
    # locahost:8000/api/v1/categorias/<int:id>  [GET, PUT, DELETE]
    # locahost:8000/api/v1/series               [GET, POST]
    # locahost:8000/api/v1/series/<int:id>      [GET, PUT, DELETE]
    path('v1/', include(router.urls)),
    # locahost:8000/api/v1/categorias/series/<int:id>      [GET]
    path('v1/categorias/series/<int:id>/', views.SeriesPorCategoriaList.as_view()),
    path('v1/favoritos/', views.FavoritoListView.as_view()),
    # Por defecto "pk" es la variable que guarde el valor del id 
    path('v1/favoritos/<int:pk>/', views.FavoritoRetrieveView.as_view()),
    # Rutas para los usuarios
    path('v1/favoritos/usuario/', views.FavoritoUsuarioListView.as_view()),
    path('v1/favoritos/usuario/<int:pk>/', views.FavoritoUsuarioRetrieveView.as_view()),
    path('v1/favoritos/usuario/crear/', views.FavoritoUsuarioCreateView.as_view()),
    path('v1/favoritos/usuario/eliminar/<int:pk>/', views.FavoritoUsuarioDeleteView.as_view())
]