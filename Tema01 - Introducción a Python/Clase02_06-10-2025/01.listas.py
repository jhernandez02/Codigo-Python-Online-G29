# Una lista es una estructura de datos
# que puede almacenar una colección de elementos

cesta = ['uva','piña','kiwi','coco']

# Mostrar el contenido de la lista
print(cesta)

# Obtener total de elementos
print(len(cesta))

# Acceder a un elemento
print(cesta[2]) # kiwi

# Modificar elemento
cesta[1] = 'melón'
print(cesta)

# Agregar un nuevo elemento
cesta.append('manzana')
cesta.append('sandía')
print(cesta)

# Eliminar un elemento
del(cesta[3])
print(cesta)