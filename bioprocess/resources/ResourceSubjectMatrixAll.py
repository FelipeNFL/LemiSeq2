import json
import logging
from flask import Response
from flask_restful import Resource
from flask_jwt_simple import jwt_required
from models.Chrompack import Chrompack
from core.slots import Slots


class ResourceSubjectMatrixAll(Resource):

    def __init__(self, **kwargs):
        self._chrompack = Chrompack(kwargs['db_connection'])

        with open('config.json', 'r') as fp:
            self._config_slots = json.loads(fp.read())

    @jwt_required
    def get(self, id_chrompack):

        try:
            samples = self._chrompack.get_samples_by_id(id_chrompack)

            if not samples:
                return Response('chrompack not found', status=400)

            slots = Slots(self._config_slots, samples)
            matrix = slots.get_matrix_busy_by_subject()

            return Response(matrix, status=200)

        except Exception as e:
            logging.error(e)
            return Response(status=500)
