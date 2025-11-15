from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Genero, Editorial, Autor, Libro
from dotenv import load_dotenv
import os

# Cargamos las variables desde el archivo .env

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
# Inicializamos la aplicación
db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/generos", methods=["GET"])
def genero_index():
    generos = Genero.query.all() # SELECT * FROM generos
    data = []#
    for genero in generos:
        data.append({
            'id':genero.id, 
            'nombre': genero.nombre,
            # Creamos el contenido mediante  una lista por compresión
            'libros': [{'id':libro.id, 'titulo': libro.titulo } for libro in genero.libros]
        })
    return jsonify(data)

@app.route("/generos", methods=["POST"])
def genero_guardar():
    data = request.json
    val_nombre = data["nombre"]
    genero = Genero(nombre=val_nombre)
    db.session.add(genero)
    db.session.commit()
    return jsonify({
        "status": "ok",
        "message": "Género creado",
        "data": {
            "id": genero.id
        }
    })

@app.route("/generos/<int:id>", methods=["GET"])
def genero_detalle(id):
    genero = Genero.query.get(id) # SELECT * FROM genero WHERE id={id}
    if genero:
        return jsonify({
            "id": genero.id,
            "nombre": genero.nombre,
            "libros": [{'id':libro.id, 'titulo': libro.titulo } for libro in genero.libros]
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Género no encontrado",
        }), 404

@app.route("/generos/<int:id>", methods=["PUT"])
def genero_editar(id):
    data = request.json
    genero = Genero.query.get(id)
    if genero:
        genero.nombre = data["nombre"]
        db.session.commit()
        return jsonify({
            "status": "ok",
            "message": "Género actualizado",
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Género no encontrado",
        }), 404

@app.route("/generos/<int:id>", methods=["DELETE"])
def genero_eliminar(id):
    genero = Genero.query.get(id)
    if genero:
        db.session.delete(genero)
        db.session.commit()
        return jsonify({
            "status": "ok",
            "message": "Género eliminado",
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Género no encontrado",
        }), 404

@app.route("/editoriales", methods=["GET"])
def editorial_index():
    editoriales = Editorial.query.all()
    data = [{'id':editorial.id, 'nombre': editorial.nombre, 'direccion': editorial.direccion, 'fecha_registro': editorial.fecha_registro} for editorial in editoriales]
    return jsonify(data)

@app.route("/editoriales/<int:id>", methods=["GET"])
def editorial_detalle(id):
    editorial = Editorial.query.get(id)
    if editorial:
        return jsonify({
            'id':editorial.id, 
            'nombre': editorial.nombre, 
            'direccion': editorial.direccion, 
            'libros': [{'id':libro.id, 'titulo': libro.titulo} for libro in editorial.libros],
            'fecha_registro': editorial.fecha_registro
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Editorial no encontrada",
        }), 404

@app.route("/editoriales", methods=["POST"])
def editorial_guardar():
    data = request.json
    val_nombre = data["nombre"]
    val_direccion = data["direccion"]
    editorial = Editorial(nombre=val_nombre, direccion=val_direccion)
    db.session.add(editorial)
    db.session.commit()
    return jsonify({
        "status": "ok",
        "message": "Editorial creada",
        "data": {
            "id": editorial.id
        }
    })

@app.route("/editoriales/<int:id>", methods=["PUT"])
def editorial_editar(id):
    data = request.json
    editorial = Editorial.query.get(id)
    if editorial:
        editorial.nombre = data["nombre"]
        editorial.direccion = data["direccion"]
        db.session.commit()
        return jsonify({
            "status": "ok",
            "message": "Editorial actualizada",
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Editorial no encontrada",
        }), 404

@app.route("/editoriales/<int:id>", methods=["DELETE"])
def editorial_eliminar(id):
    editorial = Editorial.query.get(id)
    if editorial:
        db.session.delete(editorial)
        db.session.commit()
        return jsonify({
            "status": "ok",
            "message": "Editorial eliminada",
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Editorial no encontrada",
        }), 404

@app.route("/autores", methods=["GET"])
def autor_index():
    autores = Autor.query.all()
    data = [{'id':autor.id, 'nombres': autor.nombres, 'nacionalidad': autor.nacionalidad, 'fecha_nacimiento': autor.fecha_nacimiento, 'fecha_registro': autor.fecha_registro} for autor in autores]
    return jsonify(data)

@app.route("/autores/<int:id>", methods=["GET"])
def autor_detalle(id):
    autor = Autor.query.get(id)
    if autor:
        return jsonify({
            'id':autor.id, 
            'nombres': autor.nombres, 
            'nacionalidad': autor.nacionalidad, 
            'libros': [{'id':libro.id, 'titulo': libro.titulo} for libro in autor.libros],
            'fecha_nacimiento': autor.fecha_nacimiento, 
            'fecha_registro': autor.fecha_registro
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Autor no encontrado",
        }), 404

@app.route("/autores", methods=["POST"])
def autor_guardar():
    data = request.json
    val_nombres = data["nombres"]
    val_nacionalidad = data["nacionalidad"]
    val_fecha_nacimiento = data["fecha_nacimiento"]
    autor = Autor(nombres=val_nombres, nacionalidad=val_nacionalidad, fecha_nacimiento=val_fecha_nacimiento)
    db.session.add(autor)
    db.session.commit()
    return jsonify({
        "status": "ok",
        "message": "Autor creado",
        "data": {
            "id": autor.id
        }
    })

@app.route("/autores/<int:id>", methods=["PUT"])
def autor_editar(id):
    data = request.json
    autor = Autor.query.get(id)
    if autor:
        autor.nombres = data["nombres"]
        autor.nacionalidad = data["nacionalidad"]
        autor.fecha_nacimiento = data["fecha_nacimiento"]
        db.session.commit()
        return jsonify({
            "status": "ok",
            "message": "Autor actualizado",
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Autor no encontrado",
        }), 404

@app.route("/autores/<int:id>", methods=["DELETE"])
def autor_eliminar(id):
    autor = Autor.query.get(id)
    if autor:
        db.session.delete(autor)
        db.session.commit()
        return jsonify({
            "status": "ok",
            "message": "Autor eliminado",
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Autor no encontrado",
        }), 404

@app.route("/libros", methods=["GET"])
def libro_index():
    libros = Libro.query.all()
    data = [{
        'id':libro.id, 
        'isbn': libro.isbn, 
        'titulo': libro.titulo, 
        'anio': libro.anio, 
        'genero_id':libro.genero_id, 
        'genero':libro.genero.nombre, 
        'editorial_id':libro.editorial_id, 
        'editorial':libro.editorial.nombre, 
        'autor_id': libro.autor_id, 
        'autor': libro.autor.nombres, 
        'fecha_registro': libro.fecha_registro
    } for libro in libros]
    return jsonify(data)

@app.route("/libros/<int:id>", methods=["GET"])
def libro_detalle(id):
    libro = Libro.query.get(id)
    if libro:
        return jsonify({
            'id':libro.id, 
            'isbn': libro.isbn, 
            'titulo': libro.titulo, 
            'anio': libro.anio, 
            'fecha_registro': libro.fecha_registro
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Autor no encontrado",
        }), 404

@app.route("/libros", methods=["POST"])
def libro_guardar():
    data = request.json
    val_isbn = data["isbn"]
    val_titulo = data["titulo"]
    val_anio = data["anio"]
    val_autor_id = data["autor"]
    val_genero_id = data["genero"]
    val_editorial_id = data["editorial"]
    libro = Libro(autor_id=val_autor_id, editorial_id=val_editorial_id, genero_id=val_genero_id, isbn=val_isbn, titulo=val_titulo, anio=val_anio)
    db.session.add(libro)   
    db.session.commit()
    return jsonify({
        "status": "ok",
        "message": "Libro creado",
        "data": {
            "id": libro.id
        }
    })

@app.route("/libros/<int:id>", methods=["PUT"])
def libro_editar(id):
    data = request.json
    libro = Libro.query.get(id)
    if libro:
        libro.isbn = data["isbn"]
        libro.titulo = data["titulo"]
        libro.anio = data["anio"]
        libro.autor_id = data["autor"]
        libro.genero_id = data["genero"]
        libro.editorial_id = data["editorial"]
        db.session.commit()
        return jsonify({
            "status": "ok",
            "message": "Libro actualizado",
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Libro no encontrado",
        }), 404

@app.route("/libros/<int:id>", methods=["DELETE"])
def libro_eliminar(id):
    libro = Libro.query.get(id)
    if libro:
        db.session.delete(libro)
        db.session.commit()
        return jsonify({
            "status": "ok",
            "message": "Libro eliminado",
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Libro no encontrado",
        }), 404