class Mascota:
    def __init__(self,especie,nombre):
        self.__especie = especie
        self.__nombre = nombre
    
    # Métodos getters
    @property
    def species(self):
        return self.__especie
    @property
    def name(self):
        return self.__nombre
    # Métodos setters
    @name.setter
    def name(self, nuevoNombre):
        self.__nombre = nuevoNombre

masc1 = Mascota("gato","Bigotes")
print("Especie:", masc1.species)
print("Nombre:", masc1.name)
masc1.name = "Leo"
print("Nombre:", masc1.name)
print("---------------------------------")
masc2 = Mascota("perro","Mustafa")
print("Especie:", masc2.species)
print("Nombre:", masc2.name)
masc2.name = "Rufus"
print("Nombre:", masc2.name)