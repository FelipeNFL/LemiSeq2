import json
import logging
from flask import Response
from flask_restful import Resource
from models.Chrompack import Chrompack
from flask_jwt_simple import jwt_required


class ResourceUpdateSlot(Resource):

    def __init__(self, **kwargs):
        self._chrompack = Chrompack(kwargs['db_connection'])

    @jwt_required
    def put(self, id_chrompack, slot, subject):

        try:
            samples = self._chrompack.get_samples_by_id(id_chrompack)
            new_samples = []

            for sample in samples:

                if sample['slot'] == slot:

                    if sample['subject'] == '':
                        sample['subject'] = subject
                    else:
                        return Response(status=400)

                new_samples.append(sample)

            self._chrompack.update_all_samples(id_chrompack, new_samples)

            return Response(status=200)

        except Exception as e:
            logging.error(e)
            return Response(json.dumps(str(e)), status=500)
