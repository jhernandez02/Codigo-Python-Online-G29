from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Suscripcion
from .serializers import SuscripcionSerializer, BoletaSerializer
from .permissions import IsNotSuperUser, BlockUpdate
import os
import requests

class SuscripcionViewSet(viewsets.ModelViewSet):
    queryset = Suscripcion.objects.all()
    serializer_class = SuscripcionSerializer

    def get_permissions(self):
        if self.action=='list' or self.action=='destroy':
            return [IsAdminUser()]
        elif  self.action=='create':
            return [IsNotSuperUser()]
        elif self.action=='update':
            return [BlockUpdate()]
        else: #self.action=='retrieve'
            return [IsAuthenticated()]

    def perform_create(self, serializer):
        # Obtenemos el usuario que ha enviado el token
        user = self.request.user
        serializer.save(usuario=user)

@api_view(['POST'])
def generar_boleta(request):
    serializer = BoletaSerializer(data=request.data)
    if serializer.is_valid():
        item = {
            "unidad_de_medida": "NIU",
            "descripcion": "Membresia Platinium - 1 año",
            "cantidad": 1,
            "valor_unitario": 100.00,
            "precio_unitario": 118.00,
            "subtotal": 100.00,
            "tipo_de_igv": 1,
            "igv": 18.00,
            "total": 118.00,
            "anticipo_regularizacion": False
        }
        data = {
            "operacion": "generar_comprobante",
            "tipo_de_comprobante": 2,
            "serie": "BBB1",
            "numero": 3,
            "sunat_transaction": 1,
            "cliente_tipo_de_documento": 1,
            "cliente_numero_de_documento": "87654321",
            "cliente_denominacion": "Jose Pinedo",
            "cliente_direccion": "Lima",
            "fecha_de_emision": "12-01-2026",
            "moneda": 1,
            "porcentaje_de_igv": 18.00,
            "total_igv": 18.00,
            "total_gravada": 100,
            "total": 118.00,
            "items": [item]
        }

        nubefact_url = os.getenv("NUBEFACT_URL")
        nubefact_token = os.getenv("NUBEFACT_TOKEN")
        headers = {'Authorization': 'Bearer '+nubefact_token}

        response = requests.post(url=nubefact_url, headers=headers, json=data)
        print(response.status_code)
        jsonDict = response.json()
        print(jsonDict)
        return Response({"menssage":"Boleta creada existosamente", "enlace_boleta": jsonDict['enlace_del_pdf']})