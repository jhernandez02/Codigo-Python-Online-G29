from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Inicializamos SQLAlchemy
db = SQLAlchemy()

class Genero(db.Model):
    __tablename__ = 'generos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

class Editorial(db.Model):
    __tablename__ = 'editoriales'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150),nullable=False)
    direccion = db.Column(db.String(255),nullable=True)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

class Autor(db.Model):
    __tablename__ = 'autores'
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(150), nullable=False)
    nacionalidad = db.Column(db.String(100), nullable=True)
    fecha_nacimiento = db.Column(db.Date, nullable=True)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

class Libro(db.Model):
    __tablename__ = 'libros'
    id = db.Column(db.Integer, primary_key=True)
    autor_id = db.Column(db.Integer, db.ForeignKey('autores.id'), nullable=False)
    genero_id = db.Column(db.Integer, db.ForeignKey('generos.id'), nullable=False)
    editorial_id = db.Column(db.Integer, db.ForeignKey('editoriales.id'), nullable=False)
    isbn = db.Column(db.String(25),nullable=False)
    titulo = db.Column(db.String(150),nullable=False)
    anio = db.Column(db.Date, nullable=True)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
