from flask import request
from flask_restful import Resource, reqparse

todos = {}

parser = reqparse.RequestParser()
parser.add_argument('task', required=True, help='La descripción de la tarea es obligatoria')

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        args = parser.parse_args()
        data = request.json
        todos[todo_id] = data['task']
        return {todo_id: todos[todo_id]}

class TodoList(Resource):
    def get(self):
        return todos

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(todos.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        todos[todo_id] = args['task']
        return todos[todo_id], 201