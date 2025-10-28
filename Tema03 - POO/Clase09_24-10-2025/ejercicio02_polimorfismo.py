class Empleado:
    descuentos = 0
    def calcularDescuentos(self):
        self.descuentos = self.sueldoBruto*0.1

    def calcularSueldo(self):
        self.calcularDescuentos()
        self.sueldoNeto = self.sueldoBruto - self.descuentos

    def info(self):
        print("--- Info Empleado ---")
        print(f"Empleado: {self.nombre}")
        print(f"Sueldo Bruto: {self.sueldoBruto:.2f}")
        print(f"Descuentos: {self.descuentos:.2f}")
        print(f"Sueldo Neto: {self.sueldoNeto:.2f}")

class EmpleadoFijo(Empleado):
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldoBruto = sueldo

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, horas, tarifaHora):
        self.nombre = nombre
        self.horas = horas
        self.tarifaHora = tarifaHora
    
    def calcularSueldo(self):
        self.sueldoBruto = self.horas * self.tarifaHora
        self.calcularDescuentos()
        self.sueldoNeto = self.sueldoBruto - self.descuentos

class EmpleadoPorComision(Empleado):
    def __init__(self, nombre, ventas, porcentajeComision):
        self.nombre = nombre
        self.ventas = ventas
        self.porcentajeComision = porcentajeComision

    def calcularSueldo(self):
        self.sueldoBruto = self.ventas * self.porcentajeComision
        self.calcularDescuentos()
        self.sueldoNeto = self.sueldoBruto - self.descuentos

emp1 = EmpleadoFijo("Eduardo Salva", 2500)
emp1.calcularSueldo()
emp1.info()
emp2 = EmpleadoPorHoras("Silvio Linares", 120, 15)
emp2.calcularSueldo()
emp2.info()
emp3 = EmpleadoPorComision("Karen Rodriguez", 8000, 0.10)
emp3.calcularSueldo()
emp3.info()

