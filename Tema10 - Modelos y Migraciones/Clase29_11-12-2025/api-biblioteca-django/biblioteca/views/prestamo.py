import datetime
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..models import Prestamo, PrestamoLibro, Usuario, Libro

@csrf_exempt
def listar(request):
    if request.method=='GET':
        lista = list(Prestamo.objects.values())
        return JsonResponse(lista, safe=False)

@csrf_exempt
def crear(request):
    if request.method=='POST':
        data = json.loads(request.body)
        usuarioId = data['usuario']
        librosId = data['libros']

        try:
            usuario = Usuario.objects.get(pk=usuarioId)
        except Usuario.DoesNotExist:
            return JsonResponse({"error":"Recurso usuario no encontrado"}, status=404)

        obj = Prestamo.objects.create(
            usuario = usuario,
            fecha_entrega = data['fecha_entrega'],
        )
        obj.save()

        detalle = []

        for libroId in librosId:
            libro = Libro.objects.get(pk=libroId)
            libro.disponible = "0"
            libro.save()
            detalle.append({"id":libro.id, "titulo":libro.titulo})
            PrestamoLibro(prestamo=obj, libro=libro).save()

        return JsonResponse({
            "mensaje": "Recurso creado",
            "datos": {
                "id": obj.id,
                "usuario_id": obj.usuario.id,
                "usuario_nombres": obj.usuario.nombres,
                "fecha_entrega": obj.fecha_entrega,
                "libros": detalle
            }
        }, status=201)
    
    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def mostrar(request, id):
    if request.method=='GET':
        try:
            obj = Prestamo.objects.get(pk=id)
            libros = [{"id": detalle.libro.id,"titulo": detalle.libro.titulo} for detalle in obj.detalles.all()]

            return JsonResponse({
                "id": obj.id,
                "usuario_id": obj.usuario.id,
                "usuario_nombres": obj.usuario.nombres,
                "fecha_registro": obj.fecha_registro,
                "fecha_entrega": obj.fecha_entrega,
                "fecha_devolucion": obj.fecha_devolucion,
                "libros": libros,
            })
        except Prestamo.DoesNotExist:
            return JsonResponse({"error":"Recurso no encontrado"}, status=404)
    
    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def devolver(request, id):
    if request.method=='PUT':
        try:
            obj = Prestamo.objects.get(pk=id)
            obj.fecha_devolucion = datetime.date.today() # Solo fecha
            obj.save()
            # Actualizamos a disponible los libros prestados
            for detalle in obj.detalles.all():
                libro = Libro.objects.get(pk=detalle.libro.id)
                libro.disponible = "1"
                libro.save()
            return JsonResponse({"mensaje":"Recurso actualizado"})
        except Prestamo.DoesNotExist:
            return JsonResponse({"error":"Recurso no encontrado"}, status=404)

    return JsonResponse({"error": "Método no permitido"}, status=405)