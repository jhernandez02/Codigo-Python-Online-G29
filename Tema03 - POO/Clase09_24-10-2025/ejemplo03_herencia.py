class FiguraGeometrica:
    def __init__(self, nombre, lados):
        self._nombre = nombre  # atributo protegido
        self._lados = lados    # atributo protegido
    def info(self):
        print('--- Info Figura ---')
        print(f"El {self._nombre} tiene {self._lados} lados")

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado
        super().__init__('cuadrado', '4')
    def area(self):
        area = self.lado ** 2
        print(f"Área del {self._nombre}: {area}")

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        super().__init__('triángulo', '3')
    def area(self):
        area = (self.base * self.altura)/2
        print(f"Área del {self._nombre}: {area}")

fig1 = Cuadrado(7)
#print(fig1._nombre) # No es una buena práctica
fig1.info()
fig1.area()

fig2 = Triangulo(5,8)
fig2.info()
fig2.area()