# raise es usado para lanzar una excepción de forma manual  

try:
    raise ValueError('Este es un mensaje de error personalizado')
except Exception as error:
    print('Ocurrió un error')
    print('Nombre Error: ', type(error).__name__)
    print('Descripción Error: ', error)