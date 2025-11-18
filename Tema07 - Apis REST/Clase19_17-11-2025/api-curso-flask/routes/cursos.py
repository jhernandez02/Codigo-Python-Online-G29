from flask import Blueprint, request, jsonify
from models import db, Curso

curso_router = Blueprint('cursos', __name__)

@curso_router.route("/cursos", methods=["GET"])
def curso_index():
    cursos = Curso.query.all()
    data = [{
                'id':curso.id, 
                'codigo':curso.codigo, 
                'nombre':curso.nombre, 
                'descripcion':curso.descripcion, 
                'costo':curso.costo, 
                'fecha_inicio':curso.fecha_inicio, 
                'fecha_fin':curso.fecha_fin, 
            } for curso in cursos] 
    return jsonify(data)

@curso_router.route("/cursos", methods=["POST"])
def curso_guardar():
    data = request.json
    val_categoria = data["categoria"]
    val_docente = data["docente"]
    val_codigo = data["codigo"]
    val_nombre = data["nombre"]
    val_descripcion = data["descripcion"]
    val_costo = data["costo"]
    val_fecha_inicio = data["fecha_inicio"]
    val_fecha_fin = data["fecha_fin"]
    curso = Curso(
        categoria_id=val_categoria, 
        docente_id=val_docente, 
        codigo=val_codigo, 
        nombre=val_nombre, 
        descripcion=val_descripcion, 
        costo=val_costo,
        fecha_inicio=val_fecha_inicio,
        fecha_fin=val_fecha_fin
    )
    db.session.add(curso)
    db.session.commit()
    return jsonify({
        "status": "ok",
        "message": "Curso creado",
        "data": {
            "id": curso.id
        }
    })

@curso_router.route("/cursos/<int:id>", methods=["GET"])
def curso_detalle(id):
    curso = Curso.query.get(id)
    if curso:
        return jsonify({
            "id": curso.id,
            "categoria_id": curso.categoria_id,
            "docente_id": curso.docente_id,
            "codigo": curso.codigo,
            "nombre": curso.nombre,
            "descripcion": curso.descripcion,
            "costo": curso.costo,
            "fecha_inicio": curso.fecha_inicio,
            "fecha_fin": curso.fecha_fin
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Curso no encontrado",
        }), 404

@curso_router.route("/cursos/<int:id>", methods=["PUT"])
def curso_editar(id):
    data = request.json
    curso = Curso.query.get(id)
    if curso:
        curso.categoria_id = data["categoria"]
        curso.docente_id = data["docente"]
        curso.codigo = data["codigo"]
        curso.nombre = data["nombre"]
        curso.descripcion = data["descripcion"]
        curso.costo = data["costo"]
        curso.fecha_inicio = data["fecha_inicio"]
        curso.fecha_fin = data["fecha_fin"]
        db.session.commit()
        return jsonify({
            "status": "ok",
            "message": "Curso actualizado",
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Curso no encontrado",
        }), 404

@curso_router.route("/cursos/<int:id>", methods=["DELETE"])
def curso_eliminar(id):
    curso = Curso.query.get(id)
    if curso:
        db.session.delete(curso)
        db.session.commit()
        return jsonify({
            "status": "ok",
            "message": "Curso eliminado",
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Curso no encontrado",
        }), 404