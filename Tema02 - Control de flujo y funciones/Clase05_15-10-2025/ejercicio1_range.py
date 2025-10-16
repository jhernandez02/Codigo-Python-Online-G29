def devolverMayor():
    cantidad = int(input('Ingresar la cantidad:'))
    lista = []
    for i in range(cantidad):
        numero = int(input('Ingresar número: '))
        lista.append(numero)
    return max(lista)

numMayor = devolverMayor()
print("El número mayor es:", numMayor)