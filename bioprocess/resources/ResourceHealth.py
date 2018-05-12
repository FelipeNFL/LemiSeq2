from flask import Response
from flask_restful import Resource


class ResourceHealth(Resource):

    def get(self):
        return Response('service is running', status=200)