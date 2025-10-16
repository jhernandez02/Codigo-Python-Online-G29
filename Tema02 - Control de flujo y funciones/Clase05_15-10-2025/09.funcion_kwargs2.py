def mostrarDatosMascota(nombre,tipo,**kwargs):
    print('nombre: ', nombre)
    print('tipo:', tipo)
    for key,value in kwargs.items():
        print(key,': ',value)

mostrarDatosMascota('Chuletas','cerdo',color='pinky',edad=3,raza='Pig')
