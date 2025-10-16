# Función que devuelve otra función
def crearMultiplicar(factor):
    def multiplicar(numero):
        return numero * factor
    return multiplicar

multiplicarPorDos = crearMultiplicar(2)
print(multiplicarPorDos(9))
multiplicarPorCinco = crearMultiplicar(5)
print(multiplicarPorCinco(9))