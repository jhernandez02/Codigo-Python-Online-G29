from flask import Blueprint, request, jsonify
from models import db, Matricula

matricula_router = Blueprint('matriculas', __name__)

@matricula_router.route("/matriculas", methods=["GET"])
def matricula_index():
    matriculas = Matricula.query.all()
    data = [{
                'curso_id':matricula.curso_id, 
                'alumno_id':matricula.alumno_id, 
                'costo':matricula.costo, 
                'pagado':matricula.pagado, 
            } for matricula in matriculas] 
    return jsonify(data)

@matricula_router.route("/matriculas", methods=["POST"])
def matricula_guardar():
    data = request.json
    val_curso = data["curso"]
    val_alumno = data["alumno"]
    val_costo = data["costo"]
    val_pagado = data["pagado"]
    matricula = Matricula(
        curso_id=val_curso, 
        alumno_id=val_alumno, 
        costo=val_costo,
        pagado=val_pagado,
    )
    db.session.add(matricula)
    db.session.commit()
    return jsonify({
        "status": "ok",
        "message": "Matrícula creada",
        "data": {
        }
    })

@matricula_router.route("/matriculas/<int:curso_id>/<int:alumno_id>", methods=["GET"])
def matricula_detalle(curso_id, alumno_id):
    matricula = Matricula.query.filter_by(curso_id=curso_id, alumno_id=alumno_id).first()
    if matricula:
        return jsonify({
            "curso_id": matricula.curso_id,
            "alumno_id": matricula.alumno_id,
            "costo": matricula.costo,
            "pagado": matricula.pagado,
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Matrícula no encontrada",
        }), 404

@matricula_router.route("/matriculas/<int:curso_id>/<int:alumno_id>", methods=["PUT"])
def matricula_editar(curso_id, alumno_id):
    data = request.json
    matricula = Matricula.query.filter_by(curso_id=curso_id, alumno_id=alumno_id).first()
    if matricula:
        matricula.curso_id = data["curso"]
        matricula.alumno_id = data["alumno"]
        matricula.costo = data["costo"]
        matricula.pagado = data["pagado"]
        db.session.commit()
        return jsonify({
            "status": "ok",
            "message": "Matrícula actualizada",
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Matrícula no encontrada",
        }), 404

@matricula_router.route("/matriculas/<int:curso_id>/<int:alumno_id>", methods=["DELETE"])
def matricula_eliminar(curso_id, alumno_id):
    matricula = Matricula.query.filter_by(curso_id=curso, alumno_id=alumno).first()
    if matricula:
        db.session.delete(matricula)
        db.session.commit()
        return jsonify({
            "status": "ok",
            "message": "Matrícula eliminada",
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Matrícula no encontrada",
        }), 404