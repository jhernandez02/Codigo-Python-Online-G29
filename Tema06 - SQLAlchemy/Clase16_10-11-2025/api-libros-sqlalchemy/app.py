from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Genero
from dotenv import load_dotenv
import os

# Cargamos las variables desde el archivo .env

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
# Inicializamos la aplicación
db.init_app(app)
migrate = Migrate(app, db)
