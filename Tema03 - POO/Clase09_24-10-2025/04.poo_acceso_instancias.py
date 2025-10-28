# Crear una aplicacion para el registro de prestamos de libros.
# Crear una clase Biblioteca
# La clase Biblioteca, permite verificar la disponibilidad de los libros consultando una lista de libros existente.
# Crear la clase Alumno que permite solicitar y devolver el préstamo de un libro a la vez.

class Biblioteca:

    listaLibros = ["Python Básico", "Matemáticas", "Historia Universal", "Física"]
    
    def verificarDisponibilidad(self, libro):
        return libro in self.listaLibros
    
    def prestarLibro(self, libro):
        if self.verificarDisponibilidad(libro):
            self.listaLibros.remove(libro)
            print(f"Se ha solicitado el libro {libro}")
            return True
        else:
            print(f"El libro {libro} no está disponible")
            return False
    
    def recibirLibro(self, libro):
        self.listaLibros.append(libro)
        print(f"Se ha devuelto el libro {libro}")
    
    def mostrarLibroDisponibles(self):
        if self.listaLibros:
            print("---Libros disponibles en la biblioteca---")
            for libro in self.listaLibros:
                print(f"- {libro}")
        else:
            print("No hay libros disponibles en este momento")
    
class Alumno:

    librosPrestados = []

    def __init__(self, nombre):
        self.nombre = nombre
    
    def solicitarLibro(self, libro, biblioteca):
        if biblioteca.prestarLibro(libro):
            self.librosPrestados.append(libro)
    
    def devolverLibro(self, libro, biblioteca):
        if libro in self.librosPrestados:
            self.librosPrestados.remove(libro)
            biblioteca.recibirLibro(libro)
        else:
            print(f"{self.nombre} No tiene prestado el libro {libro}")
    
    def mostrarLibrosPrestados(self):
        if self.librosPrestados:
            print("---Libros prestados de la biblioteca---")
            for libro in self.librosPrestados:
                print(f"- {libro}")
        else:
            print(f"{self.nombre} No hay libros prestados en este momento")


biblioteca = Biblioteca()
alumno = Alumno("Felipe")
biblioteca.mostrarLibroDisponibles()
alumno.solicitarLibro("Física", biblioteca)
alumno.mostrarLibrosPrestados()
biblioteca.mostrarLibroDisponibles()
alumno.devolverLibro("Física", biblioteca)
alumno.mostrarLibrosPrestados()
biblioteca.mostrarLibroDisponibles()