'''
El bucle while es una estructura de control, que repite un bloque de código
mientras se cumpla la condición.
No sep ueda determinar cuantas veces se va a repetri el código.
'''
condicion = True
cont = 0

while condicion:
    cont += 1
    numero = int(input('Ingresa un número: '))
    if numero<10:
        condicion = False

print("Repeticiones: ", cont)

