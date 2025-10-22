class Cake:
    # Atributos
    receta = ''
    ingredientes = ''
    sabor = ''
    precio = 0

# Instanciamos un objeto de la clase Cake
pastel =  Cake()
pastel.receta = "Mezclamos todos los ingredientes"
pastel.ingredientes = "Cacao"
pastel.sabor = "Chocolate"
pastel.precio = 20
print('Sabor:', pastel.sabor)
print('Precio:', pastel.precio)