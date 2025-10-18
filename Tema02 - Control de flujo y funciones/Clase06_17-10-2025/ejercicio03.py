# Crear un programa que simule las funciones básica de un cajero automático:
# Consultar saldo, depositar dinero, retirar dinero, salir
# Implementar un menú con opciones y valida entradas incorrectas

saldo = 1000

def consultarSaldo():
    return saldo

def depositarDinero(monto):
    global saldo
    saldo += monto

def retirarDinero(monto):
    global saldo
    if monto<=saldo:
        saldo -=monto
        return True
    else:
        return False

def menu():
    while True:
        print("----Menú----")
        print("1:Consultar saldo")
        print("2:Depositar dinero")
        print("3:Retirar dinero")
        print("0:Salir")
        opcion = input("Ingrese una opción: ")
        if opcion=="1":
            saldo = consultarSaldo()
            print('Saldo:', saldo)
        elif opcion=="2":
            monto = int(input("Ingrese el monto a depositar: "))
            depositarDinero(monto)
            print("¡El depósito ha sido realizado satisfactoriamente!")
        elif opcion=="3":
            monto = int(input("Ingrese el monto a retirar: "))
            resultado = retirarDinero(monto) # Es True o False
            if resultado:
                print("¡El retiro ha sido realizado satisfactoriamente!")
            else:
                print("¡Saldo insuficiente!")
        elif opcion=="0":
            print("Saliendo del programa")
            break
        else:
            print("¡Opción inválida!")

# Iniciamos el programa
menu()