import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..models import Agenda

@csrf_exempt
def listar(request):
    if request.method=='GET':
        agendas = list(Agenda.objects.values())
        return JsonResponse(agendas, safe=False)

@csrf_exempt
def crear(request):
    if request.method=='POST':
        data = json.loads(request.body)
        agenda = Agenda.objects.create(
            cliente = data['cliente'],
            medio = data['medio'],
            fecha_agenda = data['fecha_agenda']
        )
        agenda.save()
        return JsonResponse({
            "mensaje": "Agenda creada",
            "datos": {
                "id": agenda.fecha_agenda,
                "cliente": agenda.cliente,
                "medio": agenda.medio,
                "fecha_agenda": agenda.fecha_agenda
            }
        }, status=201)
    
    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def mostrar(request, id):
    if request.method=='GET':
        try:
            agenda = Agenda.objects.get(pk=id)
            return JsonResponse({
                "id": agenda.id,
                "cliente": agenda.cliente,
                "medio": agenda.medio,
                "fecha_agenda": agenda.fecha_agenda
            })
        except Agenda.DoesNotExist:
            return JsonResponse({"error":"Recurso no encontrado"}, status=404)
    
    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def editar(request, id):
    if request.method=='PUT':
        try:
            agenda = Agenda.objects.get(pk=id)
            data = json.loads(request.body)
            agenda.cliente = data['cliente']
            agenda.medio = data['medio']
            fecha_agenda = data['fecha_agenda']
            agenda.save()
            return JsonResponse({"mensaje":"Agenda actualizada"})
        except Agenda.DoesNotExist:
            return JsonResponse({"error":"Recurso no encontrado"}, status=404)

    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def eliminar(request, id):
    if request.method=='DELETE':
        try:
            agenda = Agenda.objects.get(pk=id)
            agenda.delete()
            return JsonResponse({"mensaje":"Agenda eliminada"})
        except Agenda.DoesNotExist:
            return JsonResponse({"error":"Recurso no encontrado"}, status=404)
    
    return JsonResponse({"error": "Método no permitido"}, status=405)