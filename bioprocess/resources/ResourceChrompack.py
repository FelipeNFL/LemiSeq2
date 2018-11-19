import shutil
import logging
from flask import Response
from flask_restful import Resource
from models.Chrompack import Chrompack
from flask_jwt_simple import jwt_required


class ResourceChrompack(Resource):

    def __init__(self, **kwargs):

        self._allowed_extensions = ['zip']
        self._chrompack = Chrompack(kwargs['db_connection'])
        self._work_dir = kwargs['upload_dir']

    def allowed_file(self, filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in self._allowed_extensions

    @jwt_required
    def delete(self, id):

        try:
            deleted_count = self._chrompack.delete(id)

            if not deleted_count:
                return Response('No record deleted', status=400)

            user_folder = '{work_dir}/{id}'.format(work_dir=self._work_dir, id=id)
            shutil.rmtree(user_folder)

            return Response(status=200)

        except Exception as e:
            logging.error(e)
            return Response(status=500)
