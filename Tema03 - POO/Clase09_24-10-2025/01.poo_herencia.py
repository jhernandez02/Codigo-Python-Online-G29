# La herencia permite que una clase (hija) reutilice y extienda
# el comportamiento de otra clase (padre)

class Padre:
    apellido = 'Gonzales'
    def saludar(self):
        print("¡Hola que tal!")

# La clase Hijo hereda de la clase Padre
class Hijo(Padre):
    def __init__(self, nombre):
        self.nombre = nombre

child = Hijo('Felipe')

# Accedemos al nombre y al apellido
print('Nombre:', child.nombre)
print('Apellido:', child.apellido)
child.saludar()
