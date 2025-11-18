from flask import Blueprint, request, jsonify
from models import db, Categoria

categoria_router = Blueprint('categorias', __name__)

@categoria_router.route("/categorias", methods=["GET"])
def categoria_index():
    categorias = Categoria.query.all()
    data = [{'id':categoria.id, 'nombre':categoria.nombre } for categoria in categorias] 
    return jsonify(data)

@categoria_router.route("/categorias", methods=["POST"])
def categoria_guardar():
    data = request.json
    val_nombre = data["nombre"]
    categoria = Categoria(nombre=val_nombre)
    db.session.add(categoria)
    db.session.commit()
    return jsonify({
        "status": "ok",
        "message": "Categoría creada",
        "data": {
            "id": categoria.id
        }
    })

@categoria_router.route("/categorias/<int:id>", methods=["GET"])
def categoria_detalle(id):
    categoria = Categoria.query.get(id)
    if categoria:
        return jsonify({
            "id": categoria.id,
            "nombre": categoria.nombre
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Categoría no encontrada",
        }), 404

@categoria_router.route("/categorias/<int:id>", methods=["PUT"])
def categoria_editar(id):
    data = request.json
    categoria = Categoria.query.get(id)
    if categoria:
        categoria.nombre = data["nombre"]
        db.session.commit()
        return jsonify({
            "status": "ok",
            "message": "Categoría actualizada",
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Categoría no encontrado",
        }), 404

@categoria_router.route("/categorias/<int:id>", methods=["DELETE"])
def categoria_eliminar(id):
    categoria = Categoria.query.get(id)
    if categoria:
        db.session.delete(categoria)
        db.session.commit()
        return jsonify({
            "status": "ok",
            "message": "Categoría eliminada",
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Categoría no encontrada",
        }), 404