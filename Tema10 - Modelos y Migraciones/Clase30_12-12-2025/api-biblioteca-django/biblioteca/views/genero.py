import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..models import Genero

@csrf_exempt
def listar(request):
    if request.method=='GET':
        lista = list(Genero.objects.values())
        return JsonResponse(lista, safe=False)

@csrf_exempt
def crear(request):
    if request.method=='POST':
        data = json.loads(request.body)
        obj = Genero.objects.create(
            nombre = data['nombre'],
        )
        obj.save()
        return JsonResponse({
            "mensaje": "Recurso creado",
            "datos": {
                "id": obj.id,
                "nombre": obj.nombre,
            }
        }, status=201)
    
    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def mostrar(request, id):
    if request.method=='GET':
        try:
            obj = Genero.objects.get(pk=id)
            return JsonResponse({
                "id": obj.id,
                "nombre": obj.nombre,
            })
        except Genero.DoesNotExist:
            return JsonResponse({"error":"Recurso no encontrado"}, status=404)
    
    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def editar(request, id):
    if request.method=='PUT':
        try:
            obj = Genero.objects.get(pk=id)
            data = json.loads(request.body)
            obj.nombre = data['nombre']
            obj.save()
            return JsonResponse({"mensaje":"Recurso actualizado"})
        except Genero.DoesNotExist:
            return JsonResponse({"error":"Recurso no encontrado"}, status=404)

    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def eliminar(request, id):
    if request.method=='DELETE':
        try:
            obj = Genero.objects.get(pk=id)
            obj.delete()
            return JsonResponse({"mensaje":"Recurso eliminado"})
        except Genero.DoesNotExist:
            return JsonResponse({"error":"Recurso no encontrado"}, status=404)
    
    return JsonResponse({"error": "Método no permitido"}, status=405)