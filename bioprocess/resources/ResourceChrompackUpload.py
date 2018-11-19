import os
import datetime
import logging
from flask import request, Response
from flask_restful import Resource
from models.Chrompack import Chrompack
from core.ExtractChrompack import FileInvalid
from core.ExtractChrompack import ExtractChrompack
from flask_jwt_simple import jwt_required, get_jwt


class ResourceChrompackUpload(Resource):

    def __init__(self, **kwargs):

        self._allowed_extensions = ['zip']
        self._upload_dir = kwargs['upload_dir']
        self._chrompack = Chrompack(kwargs['db_connection'])

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self._allowed_extensions

    def move_chrompack_to_work_dir(self, id_chrompack, file):

        file_chrompack = 'chrompack.zip'
        user_folder = self._upload_dir + '/' + id_chrompack

        os.mkdir(user_folder)

        absolut_filename = os.path.join(user_folder, file_chrompack)
        file.save(absolut_filename)

        return absolut_filename, user_folder

    def save_chrompack_in_db(self, request):

        if 'file' not in request.files:
            raise Exception('file to upload is not defined')

        file = request.files['file']
        title_chrompack = request.form.get('title')
        user = get_jwt()['username']
        uploaded = datetime.datetime.now()

        if file.filename == '' or not file:
            raise Exception('file to upload is not defined')

        if not self.allowed_file(file.filename):
            raise Exception('file to upload has not correct format')

        if not title_chrompack:
            raise Exception('title to upload do not be empty')

        return self._chrompack.save(title_chrompack, user, uploaded), file

    @jwt_required
    def post(self):

        try:
            id_chrompack, file = self.save_chrompack_in_db(request)
        except Exception as e:
            return Response(str(e), status=400)

        try:
            absolut_filename, user_folder = self.move_chrompack_to_work_dir(id_chrompack, file)
            extractor_files = ExtractChrompack(self._chrompack)
            samples = extractor_files.extract_samples(absolut_filename, user_folder)

            self._chrompack.update_all_samples(id_chrompack, samples)

            return Response(status=200)

        except FileInvalid:

            if id_chrompack:
                self._chrompack.delete(id_chrompack)

            return Response('the file uploaded is invalid', status=400)

        except Exception as e:
            logging.error(e)
            return Response(status=500)
