from django.urls import path
from . import views
from .views import agenda

urlpatterns = [
    #path('saludo/', views.saludo),
    #path('despedida/', views.despedida),
    #path('colores/<int:id>', views.colores),
    #path('cocinar/<str:accion>/<str:insumo>', views.cocinar),
    #path('operacion/', views.operacion),

    path('agendas/', agenda.listar),
    path('agendas/<int:id>', agenda.detalle),
]