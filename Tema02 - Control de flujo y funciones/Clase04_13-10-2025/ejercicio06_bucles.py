# 5. Elabore un algoritmo que solicite un número e imprimar el factorial del número
# Ej: 5! = 1x2x3x4x5
# Ej: 7! = 1x2x3x4x5x6x7
factorial = 1
numero = int(input('Número: '))
fin = numero + 1
for i in range(1, fin):
    factorial *=i

print(f"Factorial de {numero} es {factorial}")