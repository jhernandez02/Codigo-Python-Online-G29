from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# Inicializamos SQLAlchemy
db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(10), default='user') # user | admin
    email = db.Column(db.String(150), default='user@mail.com', nullable=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Movimiento(db.Model):
    __tablename__ = 'movimientos'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    monto = db.Column(db.Numeric(6,2), nullable=False)
    tipo = db.Column(db.String(1), nullable=False)
    descripcion = db.Column(db.String(150)) # I:ingreso, E:egreso
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    # Relación
    usuario = db.relationship('Usuario', backref='movimientos')