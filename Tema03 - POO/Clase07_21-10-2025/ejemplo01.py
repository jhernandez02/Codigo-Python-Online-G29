class Auto:
    marca= ''
    modelo=''
    placa=''
    color=''
    combustible=0 # Maximo de combustible es 100 %
    encendido = False

    def __init__(self,marca,modelo,placa,color):
        self.marca = marca,
        self.modelo = modelo
        self.placa = placa
        self.color = color

    def mostrarCombustible(self):
        print('Combustible:', self.combustible, '%')

    def echarCombustible(self, cantidad):
        self.combustible += cantidad
        self.mostrarCombustible()
    
    def encender(self):
        if self.combustible>0:
            self.encendido = True
            print('Auto encendido')
        else:
            print('Auto sin combustible')

    def avanzar(self):
        if self.encendido:
            print('Auto avanzando...')
        else:
            print("Auto apagado")

auto = Auto('Jetour','X3','ABC123','Azul')
auto.mostrarCombustible()
auto.echarCombustible(60)
auto.encender()
auto.avanzar()

