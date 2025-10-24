# Desarrollo una calculadora en POO, 
# que pueda sumar, restar, multiplicar y dividir
# Solicitar 2 valores, y solicitar la operación a realizar.
# Ej:   Ingresa el primer número: 3
#       Ingresa el segundo número: 4
#       Ingresa la operacion (S,R,M,D): M 
#       Output => 12

class Calculadora:
    # Constructor
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    # Métodos
    def sumar(self):
        return self.num1 + self.num2
    def restar(self):
        return self.num1 - self.num2
    def multiplicar(self):
        return self.num1 * self.num2
    def dividir(self):
        return self.num1 / self.num2

# Solicitamos los datos
num1 = int(input("Número1: "))
num2 = int(input("Número2: "))
# Convertimos el caracter ingresado a mayúscula con upper()
ope = input("Ingresa la operacion (S,R,M,D): ").upper()
# Creamos la calculadora
calc1 = Calculadora(num1, num2)
# Seleccionar la operacion a realizar
if ope=='S':
    print(f"La suma de {num1}+{num2} es ",calc1.sumar())
elif ope=='R':
    print(f"La resta de {num1}-{num2} es ",calc1.restar())
elif ope=='M':
    print(f"La multiplicación de {num1}x{num2} es ",calc1.multiplicar())
elif ope=='D':
    if num2==0:
        print("No se puede dividir entre cero")
    else:
        print(f"La división de {num1}/{num2} es ",calc1.dividir())
else:
    print("Operación inválida")

