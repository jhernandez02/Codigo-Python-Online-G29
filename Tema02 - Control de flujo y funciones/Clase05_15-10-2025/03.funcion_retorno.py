billetera = 10
comision = 0.5
# Función que solo retorna un resultado
def cajeroAutomaticoBCHP():
    print("Ingrese su tarjeta")
    monto = int(input("Ingresa el monto: "))
    return monto-comision

def cajeroAutomaticoBBCTO():
    comision = 1.5
    print("Ingrese su tarjeta")
    monto = int(input("Ingresa el monto: "))
    return monto-comision

def guardarDinero(dinero):
    global billetera
    billetera += dinero
    print(f"Billetera: S/ {billetera}")

dinero = cajeroAutomaticoBCHP()
guardarDinero(dinero)
dinero = cajeroAutomaticoBBCTO()
guardarDinero(dinero)