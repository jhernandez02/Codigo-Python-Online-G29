from flask import Flask
from flask_migrate import Migrate
from models import db
from dotenv import load_dotenv
import os

# Importamos las rutas
from routes.categorias import categoria_router
from routes.docentes import docente_router
from routes.alumnos import alumno_router
from routes.cursos import curso_router
from routes.matriculas import matricula_router

# Cargamos las variables desde el archivo .env
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

# Inicializamos la aplicación
db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Registramos las rutas
app.register_blueprint(categoria_router)
app.register_blueprint(docente_router)
app.register_blueprint(alumno_router)
app.register_blueprint(curso_router)
app.register_blueprint(matricula_router)