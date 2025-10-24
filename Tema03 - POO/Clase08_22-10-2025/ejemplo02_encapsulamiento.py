# Los métodos privados se usan para ocultar la logica interna que no debería ser llamada directamente por el usuario
# Los métodos públicos son los que definen la interfaz que otros pueden usar.

class Banco:
    def __init__(self, saldo):
        self.__saldo = saldo
    
    # Método publico
    def mostrarSaldo(self):
        print(f"Saldo actual: {self.__saldo}")
        # Este método público puede llamar a un método privado
        self.__registrarAcceso()
    
    # Método privado
    def __registrarAcceso(self):
        print("Acceso registrado en el sistema")

banco = Banco(100000)
banco.mostrarSaldo()
# banco.__registrarAcceso() # Error, no se puedo acceder a un método privado