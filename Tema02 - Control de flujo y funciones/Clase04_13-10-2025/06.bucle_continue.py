'''
La instrucción continue, salta el resto del código dentro del bucle
y pasa directamente a la siguiente iteración del bucle
'''

print('--Continue con for--')
numeros = (1,9,2,8,3,7,4,6,5,10)
# Mostrar los números mayores a 5
for num in numeros:
    if num<=5:
        # omite el codigo de abajo y continua a la siguiente iteración
        continue
    print(num)

print('--Continue con while--')
numero = 0
# mostrar los numero pares
while numero<8:
    numero += 1
    if numero%2!=0:
        continue
    print(numero)

