from flask import request
from flask_restful import Resource, reqparse
from models import db, Genero

def non_empty_string(value, name):
    if not value or not value.strip():
        raise ValueError()
    return value

parser = reqparse.RequestParser()
parser.add_argument(
    'nombre',
    type=non_empty_string,
    required=True,
    help='El campo nombre es obligatorio'
)

class GeneroListResource(Resource):
    def get(self):
        generos = Genero.query.all()
        return [{'id':item.id, 'nombre':item.nombre} for item in generos], 200
    
    def post(self):
        args = parser.parse_args() # Validamos los campos requeridos
        data = request.json
        genero = Genero(nombre=data['nombre'])
        db.session.add(genero)
        db.session.commit()
        return {
            'message': 'Genero creado',
            'data': {
                'id': genero.id,
                'nombre': genero.nombre
            }
        }, 201

class GeneroResource(Resource):
    def get(self, id):
        genero = Genero.query.get_or_404(id)
        return {'id':genero.id, 'nombre':genero.nombre}, 200
    
    def put(self, id):
        args = parser.parse_args() # Validamos los campos requeridos
        genero = Genero.query.get_or_404(id)
        genero.nombre = args['nombre']
        db.session.commit()
        return {
            'message': 'Genero actualizado',
            'data': {
                'id': genero.id,
                'nombre': genero.nombre
            }
        }, 200
    
    def delete(self, id):
        genero = Genero.query.get_or_404(id)
        db.session.delete(genero)
        db.session.commit()
        return {'message': 'Genero eliminado'}, 200
