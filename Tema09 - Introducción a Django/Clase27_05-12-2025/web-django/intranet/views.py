import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def saludo(request):
    return JsonResponse({
        "mensaje": "Hola!"
    })

@csrf_exempt
def despedida(request):
    if request.method=='GET':
        return JsonResponse({
            "mensaje": "Adiós!"
        })
    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def colores(request, id):
    lista = ['azul','verde','amarillo']
    if request.method=='GET':
        try:
            return JsonResponse({
                "data": lista[id]
            })
        except IndexError:
            return JsonResponse({"error": "El elemento no se encontró"}, status=404)
    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def cocinar(request, insumo, accion):
    if request.method=='GET':
        return JsonResponse({
            "mensaje": f"Vamos a {accion} {insumo}"
        })
    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def operacion(request):
    if request.method=='POST':
        operaciones = ['sumar','restar','multiplicar','dividir']
        try:
            data = json.loads(request.body)
            n1 = data['num1']
            n2 = data['num2']
            ope = data['ope']
            existe = ope in operaciones
            if not existe:
                return JsonResponse({"error": "No se encontró la operación"}, status=404)

            resultado = 0
            if ope=='sumar':
                resultado =  n1 + n2
            elif ope=='restar':
                resultado =  n1 - n2
            elif ope=='multiplicar':
                resultado =  n1 * n2
            elif ope=='dividir':
                resultado =  n1 / n2
            
            return JsonResponse({
                "n1": data['num1'],
                "n2": data['num2'],
                "ope": data['ope'],
                "result": resultado
            })
        except KeyError:
            return JsonResponse({"error": "Uno o más datos no se han enviado"}, status=404)
    return JsonResponse({"error": "Método no permitido"}, status=405)
