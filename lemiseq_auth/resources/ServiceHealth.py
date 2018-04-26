from flask_restful import Resource
from flask import Response

class ServiceHealth(Resource):

    def get(self):
        return Response('service is running', status=200)
