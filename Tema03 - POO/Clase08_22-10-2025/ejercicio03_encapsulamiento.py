# Crear una clase Empleado con los siguiente atributos:
# nombre, salario, horas_extras
# Implementar los métodos para:
# Asignar y obtener el nombre del empleado
# Asignar y obtener el salario y horas extras
# Calcular el salario total, donde cada hora extra vale el 20% más que la hora normal

class Empleado:
    def __init__(self, nombre, salario, horas_extras):
        self.__nombre = nombre
        self.__salario = salario
        self.__horas_extras = horas_extras

    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def getSalario(self):
       return self.__salario
    def setSalario(self, salario):
        self.__salario = salario
    
    def getHorasExtras(self):
       return self.__horas_extras
    def setHorasExtras(self, horas_extras):
        self.__horas_extras = horas_extras

    def __calcularValorHora(self):
        return self.__salario/160 # asumimos 160 hrs al mes
    
    def __calcularSalarioExtra(self, valor_hora_extra):
        return self.__horas_extras * valor_hora_extra
    
    def calcularSalarioTotal(self):
        valor_hora = self.__calcularValorHora()
        valor_hora_extra = valor_hora * 1.2
        salario_extra = self.__calcularSalarioExtra(valor_hora_extra)
        return self.__salario + salario_extra

empleado = Empleado("Kevin",6000,10)
print("Salario:",empleado.getSalario())
print("Horas extras:",empleado.getHorasExtras())
print("Salario total:",empleado.calcularSalarioTotal())
