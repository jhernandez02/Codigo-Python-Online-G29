from django.urls import path
from . import views
from .views import agenda, proveedor

urlpatterns = [
    #path('saludo/', views.saludo),
    #path('despedida/', views.despedida),
    #path('colores/<int:id>', views.colores),
    #path('cocinar/<str:accion>/<str:insumo>', views.cocinar),
    #path('operacion/', views.operacion),

    path('agendas/', agenda.listar),
    path('agendas/crear', agenda.crear),
    path('agendas/mostrar/<int:id>', agenda.mostrar),
    path('agendas/editar/<int:id>', agenda.editar),
    path('agendas/eliminar/<int:id>', agenda.eliminar),

    path('proveedores/', proveedor.listar),
    path('proveedores/crear', proveedor.crear),
    path('proveedores/mostrar/<int:id>', proveedor.mostrar),
    path('proveedores/editar/<int:id>', proveedor.editar),
    path('proveedores/eliminar/<int:id>', proveedor.eliminar),
]