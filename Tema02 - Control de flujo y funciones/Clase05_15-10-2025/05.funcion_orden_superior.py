'''
Una función de orden superior es una función que:
1. Recibe otra función como argumento
2. Devuelve una función como resultado
'''

def duplicar(numero):
    return numero*2

def cuadrado(numero):
    return numero**2

def ejecutarFuncion(funcion):
    numero = int(input('Ingrese el número: '))
    resultado = funcion(numero)
    print(resultado)

ejecutarFuncion(cuadrado)
ejecutarFuncion(duplicar)
