from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

generos = [
    {"id":1, "nombre":"Infantil", "fecha_registro":"2025-11-07 20:12:15"},
    {"id":2, "nombre":"Juvenil", "fecha_registro":"2025-11-07 20:12:15"}
]

libros = [
    {"id":1, "titulo":"Mi planta se murió", "isbn":"klka7y9asdf", "anio":"2015", "fecha_registro":"2025-11-07 20:12:15"},
    {"id":2, "titulo":"Vacaciones en la arena", "isbn":"53adfo82j2", "anio":"2012", "fecha_registro":"2025-11-07 20:12:15"}
]

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Recurso Generos

@app.route("/generos", methods=["GET"])
def generos_listar():
    return jsonify(generos), 200

@app.route("/generos/<int:id>", methods=["GET"])
def generos_detalle(id):
    # Aplicamos una expresion generadora para obtener el genero a buscar por su id
    genero = next((item for item in generos if item["id"]==id), None)
    if genero:
        return jsonify(genero), 200
    return jsonify({"message":"Género no encontrado"}), 404

@app.route("/generos", methods=["POST"])
def generos_crear():
    datos = request.get_json()
    # Aplicamos "list comprehension" para obtener el nuevo id
    nuevoId = max([g["id"] for g in generos], default=0)+1
    nuevoDato = {
        "id": nuevoId,
        "nombre": datos["nombre"],
        "fecha_registro": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    generos.append(nuevoDato)
    return jsonify(nuevoDato), 201

@app.route("/generos/<int:id>", methods=["PUT"])
def generos_actualizar(id):
    datos = request.get_json()
    genero = next((item for item in generos if item["id"]==id), None)
    if not genero:
        return jsonify({"message":"Género no encontrado"}), 404
    genero["nombre"] = datos["nombre"]
    return jsonify(genero), 200

@app.route("/generos/<int:id>", methods=["DELETE"])
def generos_eliminar(id):
    global generos
    genero = next((item for item in generos if item["id"]==id), None)
    if not genero:
        return jsonify({"message":"Género no encontrado"}), 404
    generos = [item for item in generos if item["id"]!=id]
    return jsonify({"message":"Género eliminado"}), 200

# Recurso Libros

@app.route("/libros", methods=["GET"])
def libros_listar():
    return jsonify(libros), 200

@app.route("/libros/<int:id>", methods=["GET"])
def libros_detalle(id):
    # Aplicamos una expresion generadora para obtener el libro a buscar por su id
    libro = next((item for item in libros if item["id"]==id), None)
    if libro:
        return jsonify(libro), 200
    return jsonify({"message":"Libro no encontrado"}), 404

@app.route("/libros", methods=["POST"])
def libros_crear():
    datos = request.get_json()
    # Aplicamos "list comprehension" para obtener el nuevo id
    nuevoId = max([item["id"] for item in libros], default=0)+1
    nuevoDato = {
        "id": nuevoId,
        "titulo": datos["titulo"],
        "isbn": datos["isbn"],
        "anio": datos["anio"],
        "fecha_registro": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    libros.append(nuevoDato)
    return jsonify(nuevoDato), 201

@app.route("/libros/<int:id>", methods=["PUT"])
def libros_actualizar(id):
    datos = request.get_json()
    libro = next((item for item in libros if item["id"]==id), None)
    if not libro:
        return jsonify({"message":"Libro no encontrado"}), 404
    libro["titulo"] = datos["titulo"]
    libro["isbn"] = datos["isbn"]
    libro["anio"] = datos["anio"]
    return jsonify(libro), 200

@app.route("/libros/<int:id>", methods=["DELETE"])
def libros_eliminar(id):
    global libros
    libro = next((item for item in libros if item["id"]==id), None)
    if not libro:
        return jsonify({"message":"Libro no encontrado"}), 404
    libros = [item for item in libros if item["id"]!=id]
    return jsonify({"message":"Libro eliminado"}), 200