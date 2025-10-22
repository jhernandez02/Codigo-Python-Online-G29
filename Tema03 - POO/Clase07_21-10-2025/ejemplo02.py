class Cake:
    # Atributos
    receta = ''
    ingredientes = ''
    sabor = ''
    precio = 0

    def __init__(self, ingredientes, receta, sabor, precio):
        self.ingredientes = ingredientes
        self.receta = receta
        self.sabor = sabor
        self.precio = precio

# Instanciamos un objeto de la clase Cake
pastel =  Cake("Cacao","Mezclamos todos los ingredientes","Chocolate",20)
print('Sabor:', pastel.sabor)
print('Precio:', pastel.precio)
print('-----------------------------------------------')
pastel2 =  Cake("Vainilla y Chocoloe","Mezclamos todos los ingredientes","Marmoleado",25)
print('Sabor:', pastel2.sabor)
print('Precio:', pastel2.precio)