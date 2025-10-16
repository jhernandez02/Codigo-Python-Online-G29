# Implementar una función que solicite
# el valor del lado de un cuadrado
# y retorne el área y el perímetro

def calcularPerimetroArea(lado):
    area = lado**2
    perimetro = lado*4
    # Retornamos 2 variables
    return area, perimetro

lado = int(input('Ingresa el lado del cuadrado: '))
val_area, val_perimetro = calcularPerimetroArea(lado)
print(f"Área: {val_area}")
print('Perímetro:', val_perimetro)