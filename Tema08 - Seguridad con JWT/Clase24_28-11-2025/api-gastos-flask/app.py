from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_mail import Mail
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

# Configuración del servidor de correo
app.config['MAIL_SERVER'] = os.getenv('MAIL_HOST')
app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USER')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASS')
app.config['MAIL_DEFAULT_SENDER'] = 'no-reply@codigo.edu.pe'

# Inicializamos
db.init_app(app)
mail = Mail(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# Importamos la rutas
from routes.auth import auth_router
from routes.movimiento import movimiento_router
from routes.password import password_router

# Registramos las rutas
app.register_blueprint(auth_router)
app.register_blueprint(movimiento_router)
app.register_blueprint(password_router)