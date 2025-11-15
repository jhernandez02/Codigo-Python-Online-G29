from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Auto
from dotenv import load_dotenv
import os

# Cargamos las variables desde el archivo .env

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
# Inicializamos la aplicación
db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/autos", methods=["GET"])
def auto_index():
    autos = Auto.query.all()
    data = [{
        'id':auto.id, 
        'marca': auto.marca, 
        'modelo': auto.modelo, 
        'placa': auto.placa, 
        'color': auto.color
    } for auto in autos]
    return jsonify(data)

@app.route("/autos/<int:id>", methods=["GET"])
def auto_detalle(id):
    auto = Auto.query.get(id)
    if auto:
        return jsonify({
            'id':auto.id, 
            'marca': auto.marca, 
            'modelo': auto.modelo, 
            'placa': auto.placa, 
            'color': auto.color
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Auto no encontrado",
        }), 404

@app.route("/autos", methods=["POST"])
def auto_guardar():
    data = request.json
    val_marca = data["marca"]
    val_modelo = data["modelo"]
    val_placa = data["placa"]
    val_color = data["color"]
    auto = Auto(marca=val_marca, modelo=val_modelo, placa=val_placa, color=val_color)
    db.session.add(auto)
    db.session.commit()
    return jsonify({
        "status": "ok",
        "message": "Auto creado",
        "data": {
            "id": auto.id
        }
    })

@app.route("/autos/<int:id>", methods=["PUT"])
def auto_editar(id):
    data = request.json
    auto = Auto.query.get(id)
    if auto:
        auto.marca = data["marca"]
        auto.modelo = data["modelo"]
        auto.placa = data["placa"]
        auto.color = data["color"]
        db.session.commit()
        return jsonify({
            "status": "ok",
            "message": "Auto actualizado",
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Auto no encontrado",
        }), 404

@app.route("/autos/<int:id>", methods=["DELETE"])
def auto_eliminar(id):
    auto = Auto.query.get(id)
    if auto:
        db.session.delete(auto)
        db.session.commit()
        return jsonify({
            "status": "ok",
            "message": "Auto eliminado",
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Auto no encontrado",
        }), 404