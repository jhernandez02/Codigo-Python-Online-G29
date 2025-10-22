class Celular:
    marca = ''
    modelo = ''
    bateria = 80
    numero = ''

    def inicializar(self, marca, modelo, numero):
        # Asignamos los valores de los parámetros a los atributos de la clase
        # self indica que pertenece a la clase
        self.marca = marca
        self.modelo = modelo
        self.numero = numero

celular1 = Celular()
celular1.inicializar('Xiaomi','Redmi 12','987654321')
print('celular1 nro:', celular1.numero)
celular2 = Celular()
celular2.inicializar('Sony','Erisson','912654456')
print('celular2 nro:', celular2.numero)