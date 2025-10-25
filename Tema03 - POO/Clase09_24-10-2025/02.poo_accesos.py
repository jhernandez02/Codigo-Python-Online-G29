# acceso público: se puede acceder desde la clase y fuera de ella (desde el objeto) 
# acceso privado: se puede acceder dentro de la clase y no se hereda
# acceso protegido (convención): se puede acceder dentro de la clase y subclase (clase hija)

class Empleado:
    def __init__(self, dni, nombre, salario):
        self.__dni = dni        # privado
        self._salario = salario # protegido
        self.nombre = nombre    # público
    
    def _info(self):
        print('--- Info Empleado ---')
        print(f"Empleado: {self.nombre}")
        print(f"Salario: {self._salario}")
    
class Gerente(Empleado):
    def __init__(self, dni, nombre, salario, area):
        super().__init__(dni, nombre, salario)
        self.area = area
    def generarInforme(self):
        self._info()
    def getDni(self):
        # No se puede hererar __dni por ser privado
        print("Dni:", self.__dni)

manager = Gerente("8765431", "Lucas", 6000, "Ventas")
manager.generarInforme()
# Si puede acceder, pero por convención no se debe
# manager._info()
# print("Dni",manager.__dni) # No se puede por ser privado
# manager.getDni() # Da error