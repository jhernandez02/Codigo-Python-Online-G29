from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

from resources.hello_world import HelloWorld
from resources.todo import TodoList, TodoSimple
from resources.calculadora import Calculadora

# Rutas
api.add_resource(HelloWorld, '/')
api.add_resource(TodoList, '/todo')
api.add_resource(TodoSimple, '/todo/<string:todo_id>') # [GET, PUT]
api.add_resource(Calculadora, '/calculadora') # [POST]
