import json
import logging
from flask import Response
from flask_restful import Resource
from flask_jwt_simple import jwt_required
from models.Chrompack import Chrompack
from core.slots import Slots


class ResourceSubjectMatrixEmpty(Resource):

    def __init__(self, **kwargs):
        self._config_slots = kwargs['configs']

    @jwt_required
    def get(self):

        try:
            slots = Slots(self._config_slots, [])
            matrix = slots.get_matrix_busy_by_subject()

            return Response(matrix, status=200)

        except Exception as e:
            logging.error(e)
            return Response(status=500)
