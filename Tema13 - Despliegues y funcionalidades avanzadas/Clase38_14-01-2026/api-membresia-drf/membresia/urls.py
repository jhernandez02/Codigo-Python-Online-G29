from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'suscripciones', views.SuscripcionViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/ventas/boleta/generar', views.generar_boleta),
]