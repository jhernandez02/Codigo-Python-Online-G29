from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('ope', required=True, help='El valor de la operación es obligatorio.')
parser.add_argument('num1', required=True, type=int, help='El valor debe ser númerico')
parser.add_argument('num2', required=True, type=int, help='El valor debe ser númerico')

class Calculadora(Resource):
    def post(self):
        args = parser.parse_args() # Aqui es donde se valida
        ope = args['ope']
        num1 = args['num1']
        num2 = args['num2']
        if ope=='S':
            result = num1 + num2
        elif ope=='M':
            result = num1 * num2
        elif ope=='R':
            result = num1 - num2
        elif ope=='D':
            result = num1 * num2
        else:
            result = "Operación no válida"
        return {
            "status": "ok",
            "data": {
                "ope": ope,
                "num1": num1,
                "num2": num2,
                "result": result
            }
        }, 200
