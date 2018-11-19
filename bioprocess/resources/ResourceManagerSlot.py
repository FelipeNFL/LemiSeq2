import json
import logging
from flask import Response
from flask_restful import Resource
from models.Chrompack import Chrompack
from flask_jwt_simple import jwt_required


class ResourceManagerSlot(Resource):

    def __init__(self, **kwargs):
        self._chrompack = Chrompack(kwargs['db_connection'])

    @jwt_required
    def delete(self, id_chrompack, slot):

        try:
            samples = self._chrompack.get_samples_by_id(id_chrompack)
            new_samples = []

            for sample in samples:

                logging.info('slot loop')
                logging.info(sample['slot'])

                if sample['slot'] == slot:
                    sample['subject'] = ''

                new_samples.append(sample)

            self._chrompack.update_all_samples(id_chrompack, new_samples)

            return Response(status=200)

        except Exception as e:
            logging.error(e)
            return Response(json.dumps(str(e)), status=500)

    @jwt_required
    def get(self, id_chrompack, slot):

        try:
            samples = self._chrompack.get_samples_by_id(id_chrompack)

            for sample in samples:
                if sample['slot'] == slot:
                    return Response(sample['subject'], status=200)

            return Response({}, status=200)

        except Exception as e:
            logging.error(e)
            return Response(json.dumps(str(e)), status=500)
