cesta = ['uva','piña','kiwi','coco']

# index(), devuelve la posición del elemento que se pasa como parámetro
# Si el elemento no existe en la lista, no devuelve un error
#posicion = cesta.index('fresa') # da error
posicion = cesta.index('kiwi')
print(posicion)

existe_fruta1 = "fresa" in cesta
existe_fruta2 = "coco" in cesta
print('Consulta fresa: ', existe_fruta1)
print('Consulta coco: ', existe_fruta2)