class Microonda:
    # Atributos
    encendido = False
    
    # Constructor
    def __init__(self, marca, capacidad, color):
        self.marca = marca
    
    def encender(self):
        if self.encendido==False:
            self.encendido = True
            print(f"Microondas {self.marca} encendido")
        else:
            print(f"El microondas {self.marca} ya está encendido")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"El microondas {self.marca} se ha apagado")

    def calentar(self, segundos):
        if self.encendido:
            print(f"Calentando la comida...")
            while segundos>0:
                print("Segundos: ", segundos)
                segundos -= 1
            print(f"¡Comida lista!")
        else:
            print("No se puede calentar: el microondas está apagado")

micro = Microonda("LG", 20, "Negro")
micro.encender()
micro.encender()
micro.calentar(10)
micro.apagar()
micro.apagar()