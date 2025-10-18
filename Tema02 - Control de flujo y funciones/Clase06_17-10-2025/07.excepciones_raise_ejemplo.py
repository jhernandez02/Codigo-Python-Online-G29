def saludar(nombre=None):
    try:
        if nombre is None:
            raise ValueError('Error! No se permite un valor nulo')
        else:
            print(f"Hola {nombre}")
    except Exception as error:
        print('------ Ocurrió un error ------')
        print('Nombre Error: ', type(error).__name__)
        print('Descripción Error: ', error)

saludar('Jhon')
saludar()