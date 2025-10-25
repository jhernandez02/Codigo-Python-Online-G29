# Encapsular es proteger los datos y controlar cómo se accede o se modifica
# la información dentro de un objeto

# Ejemplo sin encapsulamiento
'''
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Instanciamos el objeto  
per1 = Persona("Ana", 25)
# Accedemos y modificamos directamente
print("Edad:", per1.edad)
per1.edad = -5 # Esto no tiene sentido, pero es posible
print("Edad:", per1.edad)
'''
# Ejemplo con encapsulamiento
class Persona:
    # Constructor
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # atributo privado
        self.__edad = edad      # atributo privado
    
    # Método getter (para obtener el valor del atributo)
    def getEdad(self):
        return self.__edad
    
    # Método setter (para modificar el valor del atributo con control)
    def setEdad(self, nueva_edad):
        if nueva_edad>0:
            self.__edad = nueva_edad
        else:
            print("La edad debe ser positiva")
    
# Instanciamos el objeto
per1 = Persona("Ana", 25)
# Accedemos y modificamos mediante los métodos getter y setter
print("Edad:", per1.getEdad())
per1.setEdad(-5)
print("Edad:", per1.getEdad())