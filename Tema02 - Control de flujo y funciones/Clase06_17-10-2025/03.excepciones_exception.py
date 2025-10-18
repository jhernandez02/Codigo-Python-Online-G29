try:
    a = int(input('Número1: '))
    b = int(input('Número2: '))
    print("División:", a/b)
except Exception as error:
    print('Ha ocurrido en error')
    print('Nombre Error: ', type(error).__name__)
    print('Descripción Error: ', error)