# 2. Elabore un algoritmo que solicite 5 números e imprima la suma
suma = 0
for i in range(5):
    numero = int(input('Número: '))
    suma += numero

print('Suma:', suma)
