from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Suscripcion
from .serializers import SuscripcionSerializer, BoletaSerializer
from .permissions import IsNotSuperUser, BlockDelete
import os
import requests
from datetime import datetime

def generar_boleta_electronica(boletaData):
    print(boletaData)
    item = {
        "unidad_de_medida": "NIU",
        "descripcion": boletaData['item_descripcion'],
        "cantidad": 1,
        "valor_unitario": boletaData['item_precio'],
        "precio_unitario": boletaData['item_precio']*1.18,
        "subtotal": boletaData['item_precio'],
        "tipo_de_igv": 1,
        "igv": 18.00, # % porcetaje
        "total": boletaData['item_precio']*1.18,
        "anticipo_regularizacion": False
    }
    data = {
        "operacion": "generar_comprobante",
        "tipo_de_comprobante": 2,
        "serie": "BBB1",
        "numero": boletaData['nro_correlativo'],
        "sunat_transaction": 1,
        "cliente_tipo_de_documento": 1,
        "cliente_numero_de_documento": boletaData['nro_documento'],
        "cliente_denominacion": boletaData['cliente_nombres'],
        "cliente_direccion": boletaData['cliente_direccion'],
        "fecha_de_emision": datetime.now().strftime('%d-%m-%Y'),
        "moneda": 1,
        "porcentaje_de_igv": 18.00,
        "total_igv": boletaData['item_precio']*0.18,
        "total_gravada": boletaData['item_precio'],
        "total": boletaData['item_precio']*1.18,
        "items": [item]
    }

    nubefact_url = os.getenv("NUBEFACT_URL")
    nubefact_token = os.getenv("NUBEFACT_TOKEN")
    headers = {'Authorization': 'Bearer ' + nubefact_token}

    response = requests.post(url=nubefact_url, headers=headers, json=data)
    jsonDict = response.json()
    print(jsonDict)

def procesar_pago(suscripcion):
    boletaData = {
        "nro_correlativo": 4,
        "nro_documento": "87654321",
        "cliente_nombres": suscripcion.usuario.first_name,
        "cliente_direccion": "Av las Palmeras 2563 - Los Olivos",
        "item_descripcion": suscripcion.membresia.nombre,
        "item_precio": suscripcion.membresia.precio,
    }
    generar_boleta_electronica(boletaData)

class SuscripcionViewSet(viewsets.ModelViewSet):
    queryset = Suscripcion.objects.all()
    serializer_class = SuscripcionSerializer

    def get_permissions(self):
        if self.action=='list':
            return [IsAdminUser()]
        elif  self.action=='create' or self.action=='update':
            return [IsNotSuperUser()]
        elif self.action=='destroy':
            return [BlockDelete()]
        else: #self.action=='retrieve'
            return [IsAuthenticated()]

    def perform_create(self, serializer):
        # Obtenemos el usuario que ha enviado el token
        user = self.request.user
        suscripcion = serializer.save(usuario=user)
        procesar_pago(suscripcion)

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