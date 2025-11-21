from flask_restful import Resource

class HelloWorld(Resource):
    def get(self):
        return {'method': 'get'}

    def post(self):
        return {'method': 'post'}

    def put(self):
        return {'method': 'put'}

    def delete(self):
        return {'method': 'delete'}