import json
import logging
from flask import Response
from flask_restful import Resource
from models.Chrompack import Chrompack
from flask_jwt_simple import jwt_required, get_jwt


class ResourceChrompackList(Resource):

    def __init__(self, **kwargs):
        self._chrompack = Chrompack(kwargs['db_connection'])

    @jwt_required
    def get(self):

        try:
            username = get_jwt()['username']
            chrompacks = self._chrompack.get_list(username)

            for chrompack in chrompacks:
                chrompack['_id'] = str(chrompack['_id'])

            response_json = json.dumps(chrompacks)

            return Response(response_json, status=200)

        except Exception as e:
            logging.error(e)
            return Response(status=500)
