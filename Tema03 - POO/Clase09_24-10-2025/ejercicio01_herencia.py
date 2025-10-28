# Crear una aplicacion para el registro de una cuenta bancaria.
# Crear una clase Cuenta, que solicite un monto inicial
# La clase Cuenta, permite depositar y retirar un monto
# Crear la clase Cliente que extiende de la clase Cuenta
# La clase Cliente permite mostrar el saldo de la cuenta

class Cuenta:
    def __init__(self, monto):
        self.monto = monto
    def depositar(self, montoIngreso):
        self.monto += montoIngreso
        print(f"Monto depositado: {montoIngreso}")
    def retirar(self, montoRetiro):
        if montoRetiro > self.monto:
            print("Saldo insuficiente")
        else:
            self.monto -= montoRetiro
            print(f"Monto retirado: {montoRetiro}")

class Cliente(Cuenta):
    def mostrarSaldo(self):
        print(f"Saldo: {self.monto}")

cliente = Cliente(1000)
cliente.mostrarSaldo()
cliente.retirar(350)
cliente.mostrarSaldo()
cliente.depositar(500)
cliente.mostrarSaldo()