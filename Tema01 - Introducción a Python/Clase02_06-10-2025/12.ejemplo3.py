# Indicar el nombre de la fruta a eliminar
cesta = ['uva','kiwi','coco','fresa','melón']
fruta = input('Fruta: ')
existe = fruta in cesta

if existe:
    index = cesta.index(fruta)
    del(cesta[index])
    print(cesta)
else:
    print('La fruta no se encuentra en la cesta')