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
]