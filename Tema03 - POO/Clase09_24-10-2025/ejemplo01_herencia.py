class Mascota:
    nombre = ''
    especie = ''
    def comer(self):
        print(f"{self.nombre} está comiendo")
    def dormir(self):
        print(f"{self.nombre} está durmiendo")

# La clase Perro hereda de Mascota
class Perro(Mascota):
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.especie = "perro"
        self.raza = raza
    def ladrar(self):
        print("wof wof wof")

# La clase Gato hereda de Mascota
class Gato(Mascota):
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.especie = "gato"
        self.raza = raza
    def maullar(self):
        print("miau miau miau")

dog = Perro("Chiquitin", "Doberman")
print('Nombre:', dog.nombre)
print('Especie:', dog.especie)
print('Raza:', dog.raza)
dog.comer()
dog.dormir()
print("-----------------------")
cat = Gato("Bigotes", "Angora")
print('Nombre:', cat.nombre)
print('Especie:', cat.especie)
print('Raza:', cat.raza)
cat.comer()
cat.dormir()