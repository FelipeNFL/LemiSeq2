import json
from flask import Response
from flask_restful import Resource
from flask_jwt_simple import jwt_required, get_jwt
from models.User import User


class ResourceMetrics(Resource):

    def __init__(self, **kwargs):
        self._dbconnection = kwargs['db_connection']

    @jwt_required
    def get(self):
        username = get_jwt()['username']

        model_user = User(self._dbconnection, username)

        metrics = {
            'chrompacks': model_user.get_num_chrompacks(),
            'samples': model_user.get_num_samples(),
            'subjects': model_user.get_subjects()
        }

        response_json = json.dumps(metrics)

        return Response(response_json, status=200)
