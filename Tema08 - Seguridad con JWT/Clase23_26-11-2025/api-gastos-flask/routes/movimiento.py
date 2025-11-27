from flask import Blueprint, request, jsonify
from functools import wraps
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt, verify_jwt_in_request
from models import db, Movimiento

movimiento_router = Blueprint('movimiento', __name__)

def role_required(role):
    def decorator(fn):
        @wraps(fn)
        @jwt_required()
        def wrapper(*args, **kwargs):
            claims = get_jwt()
            if claims['rol']!=role:
                return jsonify({"message":"No tienes permisos para esta acción"}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator

@movimiento_router.route("/movimientos", methods=["GET"])
@jwt_required()
def movimento_index():
    current_user = get_jwt_identity()
    claims = get_jwt()
    rol = claims['rol']
    if rol=='admin':
        movimientos = Movimiento.query.all()
    else:
        movimientos = Movimiento.query.filter_by(usuario_id=current_user)
    data = [{
        'id':item.id,
        'usuario':item.usuario.username,
        'monto':item.monto,
        'tipo':item.tipo,
        'descripcion':item.descripcion,
        'fecha':str(item.fecha_registro) 
    } for item in movimientos]
    return jsonify(data)

@movimiento_router.route("/movimientos", methods=["POST"])
@jwt_required()
def movimento_guardar():
    current_user = get_jwt_identity()
    claims = get_jwt()
    rol = claims['rol']
    
    if(rol=='admin'):
        return jsonify({"message":"No tienes permisos para esta acción"}), 403
    
    current_user = get_jwt_identity()
    data = request.json
    movimiento = Movimiento(
        usuario_id = current_user,
        monto = data['monto'],
        tipo =  data['tipo'],
        descripcion = data['descripcion']
    )
    db.session.add(movimiento)
    db.session.commit()
    return jsonify({
        "message": "Movimiento creado",
        "data": {
            "id": movimiento.id
        }
    }), 201

@movimiento_router.route("/movimientos/<int:id>", methods=["GET"])
@jwt_required()
def movimento_detalle(id):
    current_user = get_jwt_identity()
    claims = get_jwt()
    rol = claims['rol']
    if rol=='admin':
        item = Movimiento.query.get(id)
    else:
        item = Movimiento.query.filter_by(id=id, usuario_id=current_user).first()
    if item:
        return jsonify({
            'id':item.id,
            'usuario':item.usuario.username,
            'monto':item.monto,
            'tipo':item.tipo,
            'descripcion':item.descripcion,
            'fecha':str(item.fecha_registro) 
        })
    else:
        return jsonify({
            "message": "Movimiento no encontrado" 
        }), 404

@movimiento_router.route("/movimientos/<int:id>", methods=["PUT"])
@role_required('user')
def movimento_editar(id):
    data = request.json
    current_user = get_jwt_identity()
    item = Movimiento.query.filter_by(id=id, usuario_id=current_user).first()
    if item:
        item.monto = data['monto'],
        item.tipo =  data['tipo'],
        item.descripcion = data['descripcion']
        db.session.commit()
        return jsonify({
            "message": "Movimiento actualizado",
        })
    else:
        return jsonify({
            "message": "Movimiento no encontrado" 
        }), 404

@movimiento_router.route("/movimientos/<int:id>", methods=["DELETE"])
@role_required('user')
def movimento_eliminar(id):
    current_user = get_jwt_identity()
    item = Movimiento.query.filter_by(id=id, usuario_id=current_user).first()
    if item:
        db.session.delete(item)
        db.session.commit()
        return jsonify({
            "message": "Movimiento eliminado",
        })
    else:
        return jsonify({
            "message": "Movimiento no encontrado" 
        }), 404