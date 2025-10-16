'''
**kwargs es una forma de manejar argumentos con nombre(clave-valor)
que son variables en numero
'''

def mostrarDatosMascota(**kwargs):
    print(kwargs, type(kwargs))
    for key,value in kwargs.items():
        print(key, value)

mostrarDatosMascota(nombre='Firulais',tipo='conejo')
mostrarDatosMascota(nombre='Chuletas',tipo='cerdo',color='pinky')