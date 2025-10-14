'''
range(inicio, fin, paso) genera una secuencia de numero enteros.
inicio (opcional): número desde donde comienza la secuencia. Por defecto es 0
fin: número donde termina la secuencia, pero no se incluye.
paso (opcional): indica el incremento entre cada número. Por defecto es 1
'''
print(range(8))

print('--Iteración con range--')
# Se repite 8 veces
for i in range(8): # El valor de i inicia en 0 y su valor máximo es 7 (8-1)
    print(i)

print('--Iteración de bloque--')
# Se repite 5 veces => (8-3)
for i in range(3,8): # El valor de i inicia en 3 y su valor máximo es 7 (8-1)
    print(i)

print('--Iteración de bloque con paso--')
# Se repite 3 veces => redondeo((11-3)/3)
for i in range(3,11,3): # El valor de i inicia en 3 y su valor máximo es 10 (11-1)
    print(i)
