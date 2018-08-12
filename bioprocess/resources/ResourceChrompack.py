import logging
from flask import Response
from flask_restful import Resource
from models.Chrompack import Chrompack
from core import defines
from flask_jwt_simple import jwt_required


class ResourceChrompack(Resource):

    def __init__(self, **kwargs):

        self._allowed_extensions = ['zip']
        self._upload_dir_chrompack = defines.DATA_CHROMPACK
        self._upload_dir_sample = defines.DATA_SAMPLE

        self._chrompack = Chrompack(kwargs['db_connection'])

    def allowed_file(self, filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in self._allowed_extensions

    @jwt_required
    def delete(self, id):

        try:
            deleted_count = self._chrompack.delete(id)

            if deleted_count:
                return Response(status=200)
            else:
                return Response('No record deleted', status=400)

        except Exception as e:
            logging.error(e)
            return Response(status=500)
