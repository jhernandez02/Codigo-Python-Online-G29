from flask import Blueprint, request, jsonify
from cryptography.fernet import Fernet
from flask_mail import Message
from models import db, Usuario
import datetime
import os
from app import mail

password_router = Blueprint('password', __name__)

FERNET_KEY = os.getenv('FERNET_KEY')
fernet = Fernet(FERNET_KEY)

def generate_reset_hash(email, expiration=3600):
    # Obtenemos el tiempo actual en segundos y le agregarmo el tiempo de expiracion
    timestamp = int(datetime.datetime.now().timestamp()) + expiration
    print('timestamp:', timestamp)
    data = f"{email}|{timestamp}".encode()
    print('data:', data)
    codigo_hash = fernet.encrypt(data)
    print('codigo_hash:', codigo_hash)
    return codigo_hash.decode()

@password_router.route('/solicitud-recuperar-contrasena', methods=['POST'])
def solicitudRecuperarContrasena():
    data = request.json
    val_user = data['user']

    # Verificamos si el usuario existe:
    usuario = Usuario.query.filter_by(username=val_user).first()

    if not usuario:
        return jsonify({
            "message": "Usuario no encontrado"
        }), 404
    
    # Generamos el enlace con el codigo hash basado en el email del usuario
    codigo_hash = generate_reset_hash(usuario.email)
    reset_url = f"http://localhost:5000/restablecer-contrasena/{codigo_hash}"
    print('reset_url:', reset_url)

    # Enviamos al usuario, el enlace por el correo
    asunto = 'Recuperación de contraseña'
    destino = [usuario.email]
    mensaje = Message(asunto, recipients=destino)
    mensaje.body = f'Haz clic en el siguiente enlace para restablecer tu contraseña: {reset_url}'
    mensaje.html = f'<p>Haz clic en el siguiente enlace para restablecer tu contraseña: <a href="{reset_url}">Recuperar</a><p>'
    mail.send(mensaje)

    return jsonify({
        "message": "Correo de recuperación enviado"
    }), 200

def verify_reset_token(token):
    decrypted_data = fernet.decrypt(token.encode()).decode()
    print('decrypted_data:', decrypted_data)
    email, token_time = decrypted_data.split('|')

    # Validamos si el tiempo de expiracion es menor al tiempo actual
    expiration = int(token_time)
    current_time = int(datetime.datetime.now().timestamp())
    if expiration < current_time:
        return None

    return email

@password_router.route('/restablecer-contrasena/<token>', methods=['POST'])
def restablecerContrasena(token):
    data = request.json
    nueva_contrasena = data['password']

    val_email = verify_reset_token(token)

    # Verificamos si se ha enviado el email o el token a expirado
    if not val_email:
        return jsonify({
            "message": "Token inválido o expirado"
        }), 404

    # Verificamos si el usuario existe:
    usuario = Usuario.query.filter_by(email=val_email).first()

    if not usuario:
        return jsonify({
            "message": "Usuario no encontrado"
        }), 404

    # Actualizamos la contraseña
    usuario.set_password(nueva_contrasena)
    db.session.commit()

    return jsonify({
        "message": "Contraseña actualizada correctamente"
    }), 200