# El polimorfismo permite usar el mismo método
# en diferentes clases, pero que cada una lo implemente
# de manera distinta

class FiguraGeometrica:
    def __init__(self, nombre, base, altura):
        self.nombre = nombre
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura

class Rectangulo(FiguraGeometrica):
    pass

class Cuadrado(FiguraGeometrica):
    pass

class Triangulo(FiguraGeometrica):
    # Aplicamos polimorfismo sobreescribiendo el método
    def area(self):
        #return (self.base * self.altura)/2
         # accedemos la area de la clase FiguraGeometrica (padre)
        return super().area()/2

fig1 = Rectangulo("rectángulo", 20, 10)
print(f"Área del {fig1.nombre}:", fig1.area())

fig2 = Triangulo("triángulo", 20, 10)
print(f"Área del {fig2.nombre}:", fig2.area())