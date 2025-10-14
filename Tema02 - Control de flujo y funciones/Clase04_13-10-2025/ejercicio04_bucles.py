# 3. Elabore un algoritmo que solicite x números e imprima la suma
suma = 0
repeticiones = int(input('Repeticiones: '))
for i in range(repeticiones):
    numero = int(input('Número: '))
    suma += numero

print('Suma:', suma)
