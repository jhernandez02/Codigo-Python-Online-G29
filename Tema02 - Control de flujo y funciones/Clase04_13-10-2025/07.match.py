estado = input('Ingresa un estado(A,P,D): ')
# Disponible a partir de la versión 3.10+
match estado:
    case 'A':
        print('Activo')
    case 'P':
        print('Pendiente')
    case 'D':
        print('Denegado')
    case _:
        print('Estado incorrecto')

