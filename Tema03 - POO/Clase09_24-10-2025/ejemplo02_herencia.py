class Vehiculos:
    encendido = False
    def __init__(self, marca, tipo):
        self.marca = marca
        self.tipo = tipo
    def encender(self):
        self.encendido = True
        print(f"{self.tipo} encendido")
    def apagar(self):
        self.encendido = False
        print(f"{self.tipo} apagado")
    def info(self):
        print("--- Info Vehículo ---")
        print('Marca:', self.marca)
        print('Tipo:', self.tipo)

# La clase Auto hereda de Vehiculos
class Auto(Vehiculos):
    def __init__(self, marca, placa):
        # Pasamos los datos al contructor de la clase Vehiculos (padre)
        super().__init__(marca, 'auto')
        self.placa = placa
    def avanzar(self):
        if self.encendido:
            print("Avanzando por la carretera")

# La clase Barco hereda de Vehiculos
class Barco(Vehiculos):
    def __init__(self, marca, camino):
        super().__init__(marca, 'barco')
        self.camino = camino
    def avanzar(self):
        if self.encendido:
            print(f"Navegando por el {self.camino}")

auto = Auto('Toyota','ABC125')
auto.info()
auto.encender()
auto.avanzar()

barco = Barco('Beneteau', 'río')
barco.info()
barco.encender()
barco.avanzar()

