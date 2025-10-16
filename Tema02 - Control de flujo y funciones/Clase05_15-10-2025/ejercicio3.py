# Elabore una función1 y una funcion2,
# que tenga como argumente una lista de N números
# donde la primera función sume todos los numeros de la lista
# y la segunda función multiplique todos los números de lista
# Ej1: funcion1([1,2,3,4]) => 10
# Ej1: funcion2([1,2,3,4]) => 24

def funcion1(lista):
    return sum(lista)

def funcion2(lista):
    multiplicacion = 1
    for num in lista:
        multiplicacion *= num
    return multiplicacion

print('Sumatoria:',funcion1([1,2,3,4]))
print('Multiplicación:',funcion2([1,2,3,4]))