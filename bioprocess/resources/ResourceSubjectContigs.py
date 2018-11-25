import json
import logging
from flask import Response
from flask_restful import Resource
from flask_jwt_simple import jwt_required
from models.Subject import Subject


class ResourceSubjectContigs(Resource):

    def __init__(self, **kwargs):
        self._work_dir = kwargs['upload_dir']

    @jwt_required
    def get(self, id_chrompack, name):

        try:

            subject = Subject(id_chrompack, self._work_dir, name)
            contigs = subject.get_results()

            response_json = json.dumps(contigs)

            return Response(response_json, status=200)

        except Exception as e:
            logging.error(e)
            return Response(json.dumps(str(e)), status=500)
