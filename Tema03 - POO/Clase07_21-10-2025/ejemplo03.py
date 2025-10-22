class Libro:
    def __init__(self, titulo, genero, autor):
        self.titulo = titulo
        self.genero = genero
        self.autor = autor
    
    def info(self):
        print('Titulo:', self.titulo)
        print('Género:', self.genero)
        print('Autor:', self.autor)

libro1 = Libro('Vacaciones en la playa de estacionamiento','Novela','Josue Lopez')
libro1.info()
print('--------------------------------------------------')
libro2 = Libro('Mi planta naranja lima limón','Terror','Silvia Gonzales')
libro2.info()