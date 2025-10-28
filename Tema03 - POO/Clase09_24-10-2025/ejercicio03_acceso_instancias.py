# Queremos que un gerente pueda aumentar el sueldo de otro empleado

class Empleado:
    def __init__(self, nombre, sueldo):
        self.__nombre = nombre
        self.__sueldo = sueldo

    def getNombre(self):
        return self.__nombre

    def getSueldo(self):
        return self.__sueldo

    def setSueldo(self, sueldo):
        self.__sueldo = sueldo

    def info(self):
        print(f"Empleado: {self.__nombre} | sueldo: {self.__sueldo:.2f}")
        

class Gerente(Empleado):
    def __init__(self, nombre, sueldo, area):
        super().__init__(nombre, sueldo)
        self.area = area
    
    def aumentarSueldoEmpleado(self, empleado, porcentaje):
        aumento = empleado.getSueldo() * (porcentaje/100)
        sueldo = empleado.getSueldo() + aumento
        empleado.setSueldo(sueldo)
        print(f"{self.getNombre()} (Gerente) aumenta el sueldo de {empleado.getNombre()} en {porcentaje} %")
        print(f"El salario de {empleado.getNombre()} ha aumentado a {sueldo:.2f}")

ana = Empleado("Ana", 2500)
luis = Gerente("Luis", 4000, "Ventas")

ana.info()
luis.aumentarSueldoEmpleado(ana, 10)
ana.info()
