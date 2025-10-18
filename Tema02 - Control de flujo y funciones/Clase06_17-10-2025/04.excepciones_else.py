# El código del bloque "else", se ejecutará sin no ha ocurrido ningún error

try:
    a = int(input('Número1: '))
    b = int(input('Número2: '))
    print("División:", a/b)
except Exception as error:
    print('Ha ocurrido en error')
    # guardo el error en error.log
else:
    print('Operación sin error')
    # guardo el error en events.log