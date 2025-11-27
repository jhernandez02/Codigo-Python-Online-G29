from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from models import db
from dotenv import load_dotenv
import os

# Cargamos las variables desde archivo .env
load_dotenv()

app = Flask(__name__)
# Configuración
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY')

# Inicializamos
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# Importamos la rutas
from routes.auth import auth_router
from routes.movimiento import movimiento_router

# Registramos las rutas
app.register_blueprint(auth_router)
app.register_blueprint(movimiento_router)