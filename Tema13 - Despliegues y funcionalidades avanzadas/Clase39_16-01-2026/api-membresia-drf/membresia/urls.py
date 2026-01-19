from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'suscripciones', views.SuscripcionViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/membresias/', views.MembresiaListView.as_view()),
    path('v1/usuario/suscripciones/', views.SuscripcionUsuarioListView.as_view()),
    path('v1/ventas/boleta/generar', views.generar_boleta),
]