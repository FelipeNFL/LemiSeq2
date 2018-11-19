import json
import logging
from flask import Response
from flask_restful import Resource
from models.Chrompack import Chrompack
from flask_jwt_simple import jwt_required, get_jwt


class ResourceSubject(Resource):

    def __init__(self, **kwargs):
        self._chrompack = Chrompack(kwargs['db_connection'])

    @jwt_required
    def get(self, id_chrompack):

        try:
            subjects = self._chrompack.get_subjects_by_id(id_chrompack)
            response_json = json.dumps(subjects)

            return Response(response_json, status=200)

        except Exception as e:
            logging.error(e)
            return Response(json.dumps(e), status=500)
