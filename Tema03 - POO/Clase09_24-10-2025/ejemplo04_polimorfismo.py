class Mascota:
    def __init__(self, raza, nombre):
        self.__raza = raza
        self.__nombre = nombre
    
    def info(self):
        print('--- Info Mascota ---')
        print(f"Nombre: {self.__nombre}")
        print(f"Raza: {self.__raza}")
        print(f"Especie: {self._especie}")
    
    def hablar(self):
        print (f"hablando...")

class Perro(Mascota):
    _especie = 'perro'
    def hablar(self):
        print("wof wof wof")

class Gato(Mascota):
    _especie = 'gato'
    def hablar(self):
        print("miau miau miau")

dog = Perro("Doberman", "Julios")
dog.info()
dog.hablar()

cat = Gato("Persa", "Leono")
cat.info()
cat.hablar()