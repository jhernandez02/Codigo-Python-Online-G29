from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Inicializamos SQLAlchemy
db = SQLAlchemy()

class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

class Docente(db.Model):
    __tablename__ = 'docentes'
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    especialidad = db.Column(db.String(100), nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

class Alumno(db.Model):
    __tablename__ = 'alumnos'
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

class Curso(db.Model):
    __tablename__ = 'cursos'
    id = db.Column(db.Integer, primary_key=True)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    docente_id = db.Column(db.Integer, db.ForeignKey('docentes.id'), nullable=False)
    codigo = db.Column(db.String(20), nullable=False)
    nombre = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.String(255), nullable=True)
    costo = db.Column(db.Numeric(6,2), nullable=False)
    fecha_inicio = db.Column(db.Date, nullable=True)
    fecha_fin = db.Column(db.Date, nullable=True)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    # Creamos las relaciones
    categoria = db.relationship('Categoria')
    docente = db.relationship('Docente')

class Matricula(db.Model):
    __tablename__ = 'matriculas'
    curso_id = db.Column(db.Integer, db.ForeignKey('cursos.id'), primary_key=True)
    alumno_id = db.Column(db.Integer, db.ForeignKey('alumnos.id'), primary_key=True)
    costo = db.Column(db.Numeric(6,2), nullable=False)
    pagado = db.Column(db.String(1), default='0')
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
