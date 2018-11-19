import json
import logging
from flask import Response
from flask_restful import Resource
from flask_jwt_simple import jwt_required
from core import defines
from models.Chrompack import Chrompack
from core.ManagerSubject import ManagerSubject


class ResourceBuildSubject(Resource):

    def __init__(self, **kwargs):
        self._work_dir = kwargs['upload_dir']
        self._chrompack = Chrompack(kwargs['db_connection'])

    def get_ab1_files_list(self, id_chrompack, subject_name):

        samples = self._chrompack.get_samples_by_id(id_chrompack)

        if not samples:
            return None

        samples_path = '{work_dir}/{chrompack}/samples'.format(work_dir=self._work_dir, chrompack=id_chrompack)

        return [samples_path + '/' + sample['filename'] for sample in samples if sample['subject'] == subject_name]

    @jwt_required
    def post(self, id_chrompack, name):

        try:

            ab1_list = self.get_ab1_files_list(id_chrompack, name)
            manager_subject = ManagerSubject(self._work_dir, id_chrompack, name)

            phred_parameter_file = defines.PHRED_PARAMETERS_FILE
            phred_bin = defines.PHRED_BIN
            phd2fas_bin = defines.PHD2FAS_BIN
            phrap_bin = defines.PHRAP_BIN

            manager_subject.build(ab1_list, phred_bin, phred_parameter_file, phd2fas_bin, phrap_bin)

        except Exception as e:
            logging.error(e)
            return Response(json.dumps(str(e)), status=500)
