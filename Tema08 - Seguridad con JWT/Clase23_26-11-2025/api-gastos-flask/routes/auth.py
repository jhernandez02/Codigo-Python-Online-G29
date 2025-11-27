from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import db, Usuario

auth_router = Blueprint('auth', __name__)

@auth_router.route("/auth/registro", methods=["POST"])
def registrar():
    data = request.json
    user = data['user']
    passwd = data['passwd']
    
    if not user or not passwd:
        return jsonify({"message": "Usuario y contraseña requeridos"}), 401
    
    if Usuario.query.filter_by(username=user).first():
        return jsonify({"message": "El usuario ya existe"})
    
    usuario = Usuario(username=user)
    usuario.set_password(data['passwd'])
    db.session.add(usuario)
    db.session.commit()

    return jsonify({"message": "Usuario registrado exitosamente"}), 201

# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@auth_router.route("/auth/login", methods=["POST"])
def login():
    user = request.json.get("user", None)
    passwd = request.json.get("pass", None)
    
    usuario = Usuario.query.filter_by(username=user).first()

    # Validamos si no existe el usuario o la contraseña es incorrecta
    if not usuario or not usuario.check_password(passwd):
        return jsonify({"message": "Credenciales incorrectas"}), 401
    
    # Generamos el token de acceso
    access_token = create_access_token(
        identity = str(usuario.id),
        additional_claims = {"rol":usuario.role, "name": usuario.username}
    )
    return jsonify(access_token=access_token)