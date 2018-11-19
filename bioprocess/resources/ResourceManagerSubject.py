import json
import logging
from flask import Response
from flask_restful import Resource
from models.Chrompack import Chrompack
from flask_jwt_simple import jwt_required
from core.ManagerSubject import ManagerSubject


class ResourceManagerSubject(Resource):

    def __init__(self, **kwargs):
        self._chrompack = Chrompack(kwargs['db_connection'])
        self._work_dir = kwargs['upload_dir']

    @jwt_required
    def post(self, id_chrompack, name):
        try:
            manager_subject = ManagerSubject(self._work_dir, id_chrompack, name)
            manager_subject.create_dirs()
            self._chrompack.add_subject(name, id_chrompack)
        except Exception as e:
            logging.error(e)
            return Response(json.dumps(str(e)), status=500)
