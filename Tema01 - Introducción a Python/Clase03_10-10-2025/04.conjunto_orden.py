colorSet = {'rojo','azul','verde','azul','amarillo','azul'}

# Ordenamos lista/conjunto
listaOrdenada = sorted(colorSet) # Devuelve una lista ordenada
print('listaOrdenada: ', listaOrdenada)

# Invertimos la lista
colorList = list(colorSet) # Convertimos el conjunto en lista
print('colorList:', colorList)
listaOrdenInverso = list(reversed(colorList))
print('listaOrdenInverso: ', listaOrdenInverso)