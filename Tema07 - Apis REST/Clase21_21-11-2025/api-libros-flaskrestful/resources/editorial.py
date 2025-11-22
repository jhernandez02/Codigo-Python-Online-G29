from flask import request
from flask_restful import Resource
from models import db, Editorial

class EditorialListResource(Resource):
    def get(self):
        editoriales = Editorial.query.all()
        return [{'id':item.id, 'nombre':item.nombre, 'direccion':item.direccion} for item in editoriales], 200
    
    def post(self):
        data = request.json
        editorial = Editorial(nombre=data['nombre'], direccion=data['direccion'])
        db.session.add(editorial)
        db.session.commit()
        return {
            'message': 'Editorial creada',
            'data': {
                'id': editorial.id,
                'nombre': editorial.nombre,
                'direccion': editorial.direccion
            }
        }, 201

class EditorialResource(Resource):
    def get(self, id):
        editorial = Editorial.query.get_or_404(id)
        return {'id':editorial.id, 'nombre':editorial.nombre, 'direccion':editorial.direccion}, 200
    
    def put(self, id):
        data = request.json
        editorial = Editorial.query.get_or_404(id)
        editorial.nombre = data['nombre']
        editorial.direccion = data['direccion']
        db.session.commit()
        return {
            'message': 'Editorial actualizada',
            'data': {
                'id': editorial.id,
                'nombre': editorial.nombre,
                'direccion': editorial.direccion
            }
        }, 200
    
    def delete(self, id):
        editorial = Editorial.query.get_or_404(id)
        db.session.delete(editorial)
        db.session.commit()
        return {'message': 'Editorial eliminada'}, 200
