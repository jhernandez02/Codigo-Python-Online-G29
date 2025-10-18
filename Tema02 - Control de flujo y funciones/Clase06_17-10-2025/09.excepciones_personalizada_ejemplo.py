# Desarollar las excepciones personalizada para una biblioteca

class BibliotecaError(Exception):
    pass

class LibroNoEncontradoError(BibliotecaError):
    pass

def buscarLibro():
    libros = ['Caperucita roja','Los 3 cerditos','Blanca Nieves']
    index = int(input('Ingrese el indice del libro:' ))
    if index<len(libros):
        print('Título:', libros[index])
    else:
        raise LibroNoEncontradoError('No se encontró el libro en el sistema')

try:
    buscarLibro()
except BibliotecaError as error:
    print('Ocurrió un error')
    print('Nombre Error: ', type(error).__name__)
    print('Descripción Error: ', error)
