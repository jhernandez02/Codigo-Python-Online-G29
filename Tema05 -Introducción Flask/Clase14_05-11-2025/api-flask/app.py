from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/usuarios", methods=["GET"])
def usuarios_listar():
    return "usuarios listar"

@app.route("/usuarios", methods=["POST"])
def usuarios_crear():
    # Obtenemos los datos enviados con el formato json
    # y automaticamente se convierte en un diccionario
    data = request.get_json()
    # Obtenemos los valores de data
    nombre = data.get("nombre")
    ciudad = data.get("ciudad")
    return f"usuario creado: {nombre}"

@app.route("/usuarios/<int:id>", methods=["GET"])
def usuarios_detalle(id):
    return f"usuario detalle: {id}"

@app.route("/usuarios/<int:id>", methods=["PUT"])
def usuarios_actualizar(id):
    # Obtenemos los datos enviados con el formato json
    # y automaticamente se convierte en un diccionario
    data = request.get_json()
    # Obtenemos los valores de data
    nombre = data.get("nombre")
    ciudad = data.get("ciudad")
    return f"usuario actualizado: {nombre}"

@app.route("/usuarios/<int:id>", methods=["DELETE"])
def usuarios_eliminar(id):
    return f"usuario eliminado: {id}"