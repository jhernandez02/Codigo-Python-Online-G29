from flask import Blueprint, request, jsonify
from models import db, Docente

docente_router = Blueprint('docentes', __name__)

@docente_router.route("/docentes", methods=["GET"])
def docente_index():
    docentes = Docente.query.all()
    data = [{
                'id':docente.id, 
                'nombres':docente.nombres, 
                'apellidos':docente.apellidos, 
                'especialidad':docente.especialidad, 
            } for docente in docentes] 
    return jsonify(data)

@docente_router.route("/docentes", methods=["POST"])
def docente_guardar():
    data = request.json
    val_nombres = data["nombres"]
    val_apellidos = data["apellidos"]
    val_especialidad = data["especialidad"]
    docente = Docente(nombres=val_nombres, apellidos=val_apellidos, especialidad=val_especialidad)
    db.session.add(docente)
    db.session.commit()
    return jsonify({
        "status": "ok",
        "message": "Docente creado",
        "data": {
            "id": docente.id
        }
    })

@docente_router.route("/docentes/<int:id>", methods=["GET"])
def docente_detalle(id):
    docente = Docente.query.get(id)
    if docente:
        return jsonify({
            "id": docente.id,
            "nombres": docente.nombres,
            "apellidos": docente.apellidos,
            "especialidad": docente.especialidad
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Docente no encontrado",
        }), 404

@docente_router.route("/docentes/<int:id>", methods=["PUT"])
def docente_editar(id):
    data = request.json
    docente = Docente.query.get(id)
    if docente:
        docente.nombres = data["nombres"]
        docente.apellidos = data["apellidos"]
        docente.especialidad = data["especialidad"]
        db.session.commit()
        return jsonify({
            "status": "ok",
            "message": "Docente actualizado",
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Docente no encontrado",
        }), 404

@docente_router.route("/docentes/<int:id>", methods=["DELETE"])
def docente_eliminar(id):
    docente = Docente.query.get(id)
    if docente:
        db.session.delete(docente)
        db.session.commit()
        return jsonify({
            "status": "ok",
            "message": "Docente eliminado",
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Docente no encontrado",
        }), 404