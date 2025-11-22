from flask import Flask, jsonify
from flask_restful import Api
from werkzeug.exceptions import NotFound, BadRequest
from models import db
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

custom_errors = {
    "NotFound": {
        "message": "Recurso no encontrado",
        "status": 404,
    },
    "Unauthorized": {
        "message": "No estás autorizado para acceder a este recurso",
        "status": 401,
    },
    "Forbidden": {
        "message": "Acceso denegado",
        "status": 403,
    },
    "InternalServerError": {
        "message": "Error interno del servidor",
        "status": 500,
    },
    "NotImplemented": {
        "message": "Funcionalidad aún no implementada",
        "status": 501,
    },
    "ServiceUnavailable": {
        "message": "Servicio temporalmente no disponible",
        "status": 503,
    },
}

# Inicializamos la aplicación
db.init_app(app)
api = Api(app, errors=custom_errors)

from resources.helloworld import HelloWorld
from resources.genero import GeneroListResource, GeneroResource
from resources.editorial import EditorialListResource, EditorialResource
from resources.autor import AutorListResource, AutorResource
from resources.libro import LibroListResource, LibroResource

api.add_resource(HelloWorld, '/')
api.add_resource(GeneroListResource, '/generos') # [GET:listado, POST]
api.add_resource(GeneroResource, '/generos/<int:id>') # [GET:detalle, PUT, DELETE]
api.add_resource(EditorialListResource, '/editoriales') # [GET:listado, POST]
api.add_resource(EditorialResource, '/editoriales/<int:id>') # [GET:detalle, PUT, DELETE]
api.add_resource(AutorListResource, '/autores') # [GET:listado, POST]
api.add_resource(AutorResource, '/autores/<int:id>') # [GET:detalle, PUT, DELETE]
api.add_resource(LibroListResource, '/libros') # [GET:listado, POST]
api.add_resource(LibroResource, '/libros/<int:id>') # [GET:detalle, PUT, DELETE]

@app.errorhandler(NotFound)
def handle_400(e):
    return jsonify({'error':'Solicitud inválida'}), 400

@app.errorhandler(NotFound)
def handle_404(e):
    return jsonify({'error':'Recurso no encontrado'}), 404

@app.errorhandler(500)
def handle_500(e):
    return jsonify({'error':'Error interno del servidor'}), 500

if __name__ == '__main__':
    app.run(debug=True)