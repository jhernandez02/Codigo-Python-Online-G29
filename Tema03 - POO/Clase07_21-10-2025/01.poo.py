# Class: Una clase es una plantilla, donde se define las características y funcionalidades de un objeto.
# Objeto: Tiene atributos (características) y métodos (funcionalidades).
# Instanciar: Es la creación de un objeto basado en una clase.

class Perro:
    # Atributos
    nombre = 'Firulais'
    especie = 'Perro'
    raza = 'Pekines'
    color = 'Marrón oscuro medio teñido claro zanahoria'
    fecha_nac = 'NS'
    # Método
    def ladrar(self):
        print('wof wof wof')
    def saltar(self):
        print('perrito saltando...')
    def comer(self):
        print('perrito comiendo su ricocan')

# Instanciamos un objeto de la clase Perro
perrito1 = Perro()
# Modificamos los atributos
perrito1.nombre = 'Salchichas'
# Accedemos a los atributos
print('Nombre:', perrito1.nombre)
print('Especie:', perrito1.especie)
# Accedemos a los métodos de la clase,
perrito1.ladrar()
perrito1.comer()

perrito2 = Perro()
perrito2.raza = 'Golden Retriever'
perrito2.color = "Dorado claro"
print('Raza:', perrito2.raza)
print('Color:', perrito2.color)
perrito2.ladrar()
perrito2.saltar()