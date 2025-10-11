# Solicitar 5 números al azar (del 1 al 20)
# Mostrar los número de menor a mayor
# No debe haber repeticiones
# Ejemplo => 12,8,16,3,7
# Output => 3,7,8,12,16

numeros = []

for i in range(5):
    num = int(input('Ingresar un número:'))
    numeros.append(num)

print('numeros:', numeros)

# Convertimos a set para eliminar los elementos repetidos
numerosSet = set(numeros)
# Ordenamos la lista
listaOrdena = sorted(numerosSet)
print(listaOrdena)