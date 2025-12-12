import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..models import Usuario

@csrf_exempt
def listar(request):
    if request.method=='GET':
        lista = list(Usuario.objects.values())
        return JsonResponse(lista, safe=False)

@csrf_exempt
def crear(request):
    if request.method=='POST':
        data = json.loads(request.body)
        obj = Usuario.objects.create(
            nombres = data['nombres'],
        )
        obj.save()
        return JsonResponse({
            "mensaje": "Recurso creado",
            "datos": {
                "id": obj.id,
                "nombres": obj.nombres,
            }
        }, status=201)
    
    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def mostrar(request, id):
    if request.method=='GET':
        try:
            obj = Usuario.objects.get(pk=id)
            return JsonResponse({
                "id": obj.id,
                "nombres": obj.nombres,
            })
        except Usuario.DoesNotExist:
            return JsonResponse({"error":"Recurso no encontrado"}, status=404)
    
    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def editar(request, id):
    if request.method=='PUT':
        try:
            obj = Usuario.objects.get(pk=id)
            data = json.loads(request.body)
            obj.nombres = data['nombres']
            obj.save()
            return JsonResponse({"mensaje":"Recurso actualizado"})
        except Usuario.DoesNotExist:
            return JsonResponse({"error":"Recurso no encontrado"}, status=404)

    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def eliminar(request, id):
    if request.method=='DELETE':
        try:
            obj = Usuario.objects.get(pk=id)
            obj.delete()
            return JsonResponse({"mensaje":"Recurso eliminado"})
        except Usuario.DoesNotExist:
            return JsonResponse({"error":"Recurso no encontrado"}, status=404)
    
    return JsonResponse({"error": "Método no permitido"}, status=405)