'''
Una lista de comprensión en Python es una forma concisa 
y legible de crear listas nuevas a partir de iterables existentes, 
aplicando una expresión a cada elemento y filtrándolos condicionalmente, 
todo en una sola línea de código. 
Esta sintaxis reemplaza bucles for tradicionales y es más eficiente para tareas simples, 
ya que condensa el proceso de iteración, aplicación de la expresión 
y almacenamiento de resultados. 
'''

# Sin compresión
'''
cuadrados = []
for x in range(10):
    cuadrados.append(x**2)
'''
# Con compresion
cuadrados = [x**2 for x in range(10)]
print(cuadrados)