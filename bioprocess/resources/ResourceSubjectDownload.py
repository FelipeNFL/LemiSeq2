import os
import json
import logging
from flask import Response, send_from_directory, current_app
from flask_restful import Resource
from flask_jwt_simple import jwt_required
from models.Subject import Subject


class ResourceSubjectDownload(Resource):

    def __init__(self, **kwargs):
        self._work_dir = kwargs['upload_dir']

    @jwt_required
    def get(self, id_chrompack, name):

        try:

            subject = Subject(id_chrompack, self._work_dir, name)
            subject.create_zip()

            dir = os.path.join(current_app.root_path, subject.get_subject_dir_path())
            filename = subject.get_zip_filename()

            return send_from_directory(directory=dir, filename=filename)

        except Exception as e:
            logging.error(e)
            return Response(json.dumps(str(e)), status=500)
