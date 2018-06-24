import os
import datetime
import logging
from flask import request, Response
from flask_restful import Resource
from models.Chrompack import Chrompack
from models.Chrompack import FileInvalid
from core import defines
from flask_jwt_simple import jwt_required, get_jwt


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
    def post(self):

        try:
            if 'file' not in request.files:
                return Response('file to upload is not defined', status=400)

            file = request.files['file']
            title_chrompack = request.form.get('title')
            user = get_jwt()['username']
            uploaded = datetime.datetime.now()

            if file.filename == '' or not file:
                return Response('file to upload is not defined', status=400)

            if not self.allowed_file(file.filename):
                return Response('file to upload has not correct format', status=400)

            if not title_chrompack:
                return Response('title to upload do not be empty', status=400)

            id_chrompack = self._chrompack.save(title_chrompack, user, uploaded)
            file_chrompack = self._chrompack.get_filename(id_chrompack)
            absolut_filename = os.path.join(self._upload_dir_chrompack, file_chrompack)

            file.save(absolut_filename)

            self._chrompack.extract_samples(absolut_filename, id_chrompack, self._upload_dir_sample)

            return Response(status=200)
        except FileInvalid:
            return Response('the file uploaded is invalid', status=400)
        except Exception as e:
            logging.info(e)
            return Response(status=500)
