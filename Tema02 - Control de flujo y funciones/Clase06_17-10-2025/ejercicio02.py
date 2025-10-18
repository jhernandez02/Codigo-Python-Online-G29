# Crear un juego en el que el programa genera un número aleatorio entre 1 y 20,
# y el jugador tiene que adivinar el número.
# El programa debe indicar si el número ingresado es mayor o menor al número secreto, 
# hasta que el jugador acierte el número y se muestra la cantidad de intentos.
# Usar funciones
# Ej: Numero secreto => 15
# Adivina un número entre el 1 y 20: 10
# El numero que ingresate es menor
# Adivina un número entre el 1 y 20: 15
# Acertarse en 2 intentos!

import random

def jugar():
    numeroRandom = random.randint(1,20)
    print('Número secreto:',numeroRandom)
    intentos = 0
    while True:
        intentos += 1 # aumentamos el valor de intentos
        numero = int(input('Adivina un número entre 1 y el 20: '))
        if numero==numeroRandom:
            print(f"¡Adivinaste en {intentos} intentos!")
            break
        elif numero>numeroRandom:
            print("El numero que ingresate es mayor")
        else:
            print("El numero que ingresate es menor")

jugar()