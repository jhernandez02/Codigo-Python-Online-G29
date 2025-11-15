from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Inicializamos SQLAlchemy
db = SQLAlchemy()

class Auto(db.Model):
    __tablename__ = 'autos'
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(50), nullable=False)
    modelo = db.Column(db.String(50), nullable=False)
    placa = db.Column(db.String(6), nullable=False)
    color = db.Column(db.String(50), nullable=False)

