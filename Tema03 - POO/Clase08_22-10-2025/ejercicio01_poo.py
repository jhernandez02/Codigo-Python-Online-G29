# Desarrollo una aplicación en POO, que halle el perímetro y area
# de un cuadrado solicitando solo el valor del lado del cuadrado.

class Cuadrado:
    # Constructor
    def __init__(self, lado):
        self.lado = lado
        print("El lado del cuadrado es:", lado)
    # Métodos
    def area(self):
        return self.lado**2
    def perimetro(self):
        return self.lado*4

lado = int(input("Ingresar el valor del lado: "))
c1 = Cuadrado(lado)
print("Perimetro:",c1.perimetro())
print("Área:",c1.area())