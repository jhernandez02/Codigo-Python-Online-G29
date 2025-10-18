# El bloque finally se ejecutará siempre,
# sin importar si hay excepciones o no.

try:
    a = int(input('Número1: '))
    b = int(input('Número2: '))
    print("División:", a/b)
except:
    print('Se ha producido un error')
finally:
    print('Terminó de ejecutarse la operación')
    # guardo el error en events.log