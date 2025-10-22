# El constructor es el primer método que se ejecuta de manera automática
# cuando se instancia un objeto
class Celular:
    marca = ''
    modelo = ''
    bateria = 80
    numero = ''

    def __init__(self, marca, modelo, numero):
        # Asignamos los valores de los parámetros a los atributos de la clase
        # self indica que pertenece a la clase
        self.marca = marca
        self.modelo = modelo
        self.numero = numero
    
    def info(self):
        print('Marca:', self.marca)
        print('Modelo:', self.modelo)
        print('Batería:', self.bateria,'%')
        print('Número:', self.numero)
        print('----------------------------')

celular1 = Celular('Xiaomi','Redmi 12','987654321')
celular1.info()
celular2 = Celular('Sony','Erisson','912654456')
celular2.info()