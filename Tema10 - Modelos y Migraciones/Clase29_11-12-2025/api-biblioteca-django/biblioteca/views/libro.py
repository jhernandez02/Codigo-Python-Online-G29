import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..models import Libro, Genero

@csrf_exempt
def listar(request):
    if request.method=='GET':
        lista = list(Libro.objects.values())
        return JsonResponse(lista, safe=False)

@csrf_exempt
def crear(request):
    if request.method=='POST':
        data = json.loads(request.body)
        generoId = data['genero']

        try:
            genero = Genero.objects.get(pk=generoId)
        except Genero.DoesNotExist:
            return JsonResponse({"error":"Recurso género no encontrado"}, status=404)

        obj = Libro.objects.create(
            genero = genero,
            isbn = data['isbn'],
            titulo = data['titulo'],
            autor = data['autor'],
            disponible = data['disponible'],
        )
        obj.save()
        return JsonResponse({
            "mensaje": "Recurso creado",
            "datos": {
                "id": obj.id,
                "genero_id": obj.genero.id,
                "genero_nombre": obj.genero.nombre,
                "isbn": obj.isbn,
                "titulo": obj.titulo,
                "autor": obj.autor,
                "disponible": obj.disponible,
            }
        }, status=201)
    
    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def mostrar(request, id):
    if request.method=='GET':
        try:
            obj = Libro.objects.get(pk=id)
            return JsonResponse({
                "id": obj.id,
                "genero_id": obj.genero.id,
                "genero_nombre": obj.genero.nombre,
                "isbn": obj.isbn,
                "titulo": obj.titulo,
                "autor": obj.autor,
                "disponible": obj.disponible,
            })
        except Libro.DoesNotExist:
            return JsonResponse({"error":"Recurso no encontrado"}, status=404)
    
    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def editar(request, id):
    if request.method=='PUT':
        try:
            obj = Libro.objects.get(pk=id)
            data = json.loads(request.body)
            generoId = data['genero']

            try:
                genero = Genero.objects.get(pk=generoId)
            except Genero.DoesNotExist:
                return JsonResponse({"error":"Recurso género no encontrado"}, status=404)

            obj.genero = genero
            obj.isbn = data['isbn']
            obj.titulo = data['titulo']
            obj.autor = data['autor']
            obj.disponible = data['disponible']
            obj.save()
            return JsonResponse({"mensaje":"Recurso actualizado"})
        except Libro.DoesNotExist:
            return JsonResponse({"error":"Recurso no encontrado"}, status=404)

    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def eliminar(request, id):
    if request.method=='DELETE':
        try:
            obj = Libro.objects.get(pk=id)
            obj.delete()
            return JsonResponse({"mensaje":"Recurso eliminado"})
        except Libro.DoesNotExist:
            return JsonResponse({"error":"Recurso no encontrado"}, status=404)
    
    return JsonResponse({"error": "Método no permitido"}, status=405)