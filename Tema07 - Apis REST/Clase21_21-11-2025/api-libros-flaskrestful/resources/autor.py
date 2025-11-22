from flask import request
from flask_restful import Resource
from models import db, Autor

class AutorListResource(Resource):
    def get(self):
        autores = Autor.query.all()
        return [{
            'id':item.id, 
            'nombres':item.nombres, 
            'nacionalidad':item.nacionalidad,
            'fecha_nacimiento':item.fecha_nacimiento.strftime('%d/%m/%Y')
        } for item in autores], 200
    
    def post(self):
        data = request.json
        autor = Autor(nombres=data['nombres'], nacionalidad=data['nacionalidad'], fecha_nacimiento=data['fecha_nacimiento'])
        db.session.add(autor)
        db.session.commit()
        return {
            'message': 'Autor creado',
            'data': {
                'id': autor.id,
                'nombres': autor.nombres,
                'nacionalidad': autor.nacionalidad,
                'fecha_nacimiento': autor.fecha_nacimiento.isoformat()
            }
        }, 201

class AutorResource(Resource):
    def get(self, id):
        autor = Autor.query.get_or_404(id)
        return {
            'id':autor.id, 
            'nombres':autor.nombres, 
            'nacionalidad':autor.nacionalidad, 
            'fecha_nacimiento':str(autor.fecha_nacimiento)
        }, 200
    
    def put(self, id):
        data = request.json
        autor = Autor.query.get_or_404(id)
        autor.nombres = data['nombres']
        autor.nacionalidad = data['nacionalidad']
        autor.fecha_nacimiento = data['fecha_nacimiento']
        db.session.commit()
        return {
            'message': 'Autor actualizado',
            'data': {
                'id': autor.id,
                'nombres': autor.nombres,
                'nacionalidad': autor.nacionalidad,
                'fecha_nacimiento': str(autor.fecha_nacimiento)
            }
        }, 200
    
    def delete(self, id):
        autor = Autor.query.get_or_404(id)
        db.session.delete(autor)
        db.session.commit()
        return {'message': 'Autor eliminado'}, 200
