'''
Una excepción personalizada es útil para manejar errores específicos de tu aplicación
Puedes crear excepciones personalizadas definiendo una clase que herede de Exception
'''

class MiError(Exception):
    pass

try:
    # Lanzamos la excepcion de manera manual
    raise MiError('Ocurrió un error personalizado')
except Exception as error:
    print('Ocurrió un error')
    print('Nombre Error: ', type(error).__name__)
    print('Descripción Error: ', error)
