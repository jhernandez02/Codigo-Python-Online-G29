from flask import request
from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from models import db, Libro

class LibroListResource(Resource):
    def get(self):
        libros = Libro.query.all()
        data = [{
            'id':item.id, 
            'autor_id':item.autor_id,
            'genero_id':item.genero_id,
            'editorial_id':item.editorial_id,
            'isbn':item.isbn, 
            'titulo':item.titulo, 
            'anio':item.anio.strftime('%Y')
        } for item in libros]

        return data, 200
    
    def post(self):
        data = request.json
        try:
            libro = Libro(
                autor_id=data['autor_id'],
                genero_id=data['genero_id'],
                editorial_id=data['editorial_id'],
                isbn=data['isbn'], 
                titulo=data['titulo'], 
                anio=data['anio']
            )
            db.session.add(libro)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            print('IntegrityError:', str(e))
            return {'error': 'El autor, género o editorial es incorrecto'}, 400
        except SQLAlchemyError as e:
            db.session.rollback()
            print('SQLAlchemyError:', str(e))
            return {'error': 'Ocurrió un error interno'}, 500
        
        return {
            'message': 'Libro creado',
            'data': {
                'id': libro.id,
                'autor_id':libro.autor_id,
                'genero_id':libro.genero_id,
                'editorial_id':libro.editorial_id,
                'isbn': libro.isbn,
                'titulo': libro.titulo,
                'anio': libro.anio.strftime('%Y'),
            }
        }, 201

class LibroResource(Resource):
    def get(self, id):
        libro = Libro.query.get_or_404(id)
        return {
            'id':id, 
            'autor_id':libro.autor_id,
            'genero_id':libro.genero_id,
            'editorial_id':libro.editorial_id,
            'isbn':libro.isbn, 
            'titulo':libro.titulo, 
            'anio':libro.anio.strftime('%Y')
        }, 200
    
    def put(self, id):
        data = request.json
        libro = Libro.query.get_or_404(id)
        libro.autor_id = data['autor_id']
        libro.genero_id = data['genero_id']
        libro.editorial_id = data['editorial_id']
        libro.isbn = data['isbn']
        libro.titulo = data['titulo']
        libro.anio = data['anio']
        db.session.commit()
        return {
            'message': 'Libro actualizado',
            'data': {
                'id': libro.id,
                'autor_id':libro.autor_id,
                'genero_id':libro.genero_id,
                'editorial_id':libro.editorial_id,
                'isbn':libro.isbn, 
                'titulo':libro.titulo, 
                'anio':libro.anio.strftime('%Y')
            }
        }, 200
    
    def delete(self, id):
        libro = Libro.query.get_or_404(id)
        try:
            db.session.delete(libro)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            print('SQLAlchemyError:', str(e))
            return {'error': 'Ocurrió un error interno'}, 500
        
        return {'message': 'Libro eliminado'}, 200
        
        
