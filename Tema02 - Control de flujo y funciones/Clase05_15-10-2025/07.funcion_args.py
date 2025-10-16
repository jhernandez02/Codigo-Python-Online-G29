'''
args es una forma de pasar un número de variable de argumentos a un función
'''

def promediarNota(*args):
    print(args, type(args))
    total = len(args)
    suma = sum(args)
    promedio = suma/total
    return promedio

def entregarPromedioCursoAlgoritmos():
    resultado = promediarNota(15,18,12,10)
    print("Promedio Algoritmos:", resultado)

def entregarPromedioCursoBaseDatos():
    resultado = promediarNota(1,15,13,18,15,17,19)
    print("Promedio Base de datos:", resultado)

# Ejecutamos las funciones
entregarPromedioCursoAlgoritmos()
entregarPromedioCursoBaseDatos()
