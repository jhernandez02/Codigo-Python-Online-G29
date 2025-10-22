class Celular:
    marca = 'Xiaomi'
    modelo = 'Redmi 12'
    bateria = 80
    numero = '987564321'

    def info(self):
        print('Marca:', self.marca)
        print('Modelo:', self.modelo)
        print('Batería:', self.bateria,'%')
        print('Número:', self.numero)

    def llamar(self, numero):
        print(f"Llamando al número {numero}...")

    def enviarSmS(self, numero, texto):
        print(f"Enviando sms: '{texto}' al número: {numero}")

# Instanciamos el objeto de la clase Celular
celular = Celular()
celular.info()
celular.llamar('98798797')
celular.enviarSmS('99988877', 'Hola mundo')