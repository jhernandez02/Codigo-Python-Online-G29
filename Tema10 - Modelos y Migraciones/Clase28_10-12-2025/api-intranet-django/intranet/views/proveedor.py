import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..models import Proveedor

@csrf_exempt
def listar(request):
    if request.method=='GET':
        proveedores = list(Proveedor.objects.values())
        return JsonResponse(proveedores, safe=False)

@csrf_exempt
def crear(request):
    if request.method=='POST':
        data = json.loads(request.body)
        proveedor = Proveedor.objects.create(
            nombre = data['nombre'],
            servicio = data['servicio'],
            direccion = data['direccion'],
            contacto_nombre = data['contacto_nombre'],
            contacto_telefono = data['contacto_telefono'],
            contacto_cargo = data['contacto_cargo'],
        )
        proveedor.save()
        return JsonResponse({
            "mensaje": "Recurso creado",
            "datos": {
                "id": proveedor.id,
                "nombre": proveedor.nombre,
                "direccion": proveedor.direccion,
                "contacto_nombre": proveedor.contacto_nombre,
                "contacto_telefono": proveedor.contacto_telefono,
                "contacto_cargo": proveedor.contacto_cargo
            }
        }, status=201)
    
    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def mostrar(request, id):
    if request.method=='GET':
        try:
            proveedor = Proveedor.objects.get(pk=id)
            return JsonResponse({
                "id": proveedor.id,
                "nombre": proveedor.nombre,
                "direccion": proveedor.direccion,
                "contacto_nombre": proveedor.contacto_nombre,
                "contacto_telefono": proveedor.contacto_telefono,
                "contacto_cargo": proveedor.contacto_cargo
            })
        except Proveedor.DoesNotExist:
            return JsonResponse({"error":"Recurso no encontrado"}, status=404)
    
    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def editar(request, id):
    if request.method=='PUT':
        try:
            proveedor = Proveedor.objects.get(pk=id)
            data = json.loads(request.body)
            proveedor.nombre = data['nombre']
            proveedor.direccion = data['direccion']
            proveedor.contacto_nombre = data['contacto_nombre']
            proveedor.contacto_telefono = data['contacto_telefono']
            proveedor.contacto_cargo = data['contacto_cargo']
            proveedor.save()
            return JsonResponse({"mensaje":"Recurso actualizado"})
        except Proveedor.DoesNotExist:
            return JsonResponse({"error":"Recurso no encontrado"}, status=404)

    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def eliminar(request, id):
    if request.method=='DELETE':
        try:
            proveedor = Proveedor.objects.get(pk=id)
            proveedor.delete()
            return JsonResponse({"mensaje":"Recurso eliminado"})
        except Proveedor.DoesNotExist:
            return JsonResponse({"error":"Recurso no encontrado"}, status=404)
    
    return JsonResponse({"error": "Método no permitido"}, status=405)