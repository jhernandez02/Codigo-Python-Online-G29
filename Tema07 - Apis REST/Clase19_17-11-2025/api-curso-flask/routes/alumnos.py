from flask import Blueprint, request, jsonify
from models import db, Alumno

alumno_router = Blueprint('alumnos', __name__)

@alumno_router.route("/alumnos", methods=["GET"])
def alumno_index():
    alumnos = Alumno.query.all()
    data = [{
                'id':alumno.id, 
                'nombres':alumno.nombres, 
                'apellidos':alumno.apellidos, 
                'email':alumno.email, 
            } for alumno in alumnos] 
    return jsonify(data)

@alumno_router.route("/alumnos", methods=["POST"])
def alumno_guardar():
    data = request.json
    val_nombres = data["nombres"]
    val_apellidos = data["apellidos"]
    val_email = data["email"]
    alumno = Alumno(nombres=val_nombres, apellidos=val_apellidos, email=val_email)
    db.session.add(alumno)
    db.session.commit()
    return jsonify({
        "status": "ok",
        "message": "Alumno creado",
        "data": {
            "id": alumno.id
        }
    })

@alumno_router.route("/alumnos/<int:id>", methods=["GET"])
def alumno_detalle(id):
    alumno = Alumno.query.get(id)
    if alumno:
        return jsonify({
            "id": alumno.id,
            "nombres": alumno.nombres,
            "apellidos": alumno.apellidos,
            "email": alumno.email
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Alumno no encontrado",
        }), 404

@alumno_router.route("/alumnos/<int:id>", methods=["PUT"])
def alumno_editar(id):
    data = request.json
    alumno = Alumno.query.get(id)
    if alumno:
        alumno.nombres = data["nombres"]
        alumno.apellidos = data["apellidos"]
        alumno.email = data["email"]
        db.session.commit()
        return jsonify({
            "status": "ok",
            "message": "Alumno actualizado",
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Alumno no encontrado",
        }), 404

@alumno_router.route("/alumnos/<int:id>", methods=["DELETE"])
def alumno_eliminar(id):
    alumno = Alumno.query.get(id)
    if alumno:
        db.session.delete(alumno)
        db.session.commit()
        return jsonify({
            "status": "ok",
            "message": "Alumno eliminado",
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Alumno no encontrado",
        }), 404