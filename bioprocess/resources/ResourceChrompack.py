import os
import datetime
from zipfile import ZipFile
from flask import request, Response
from flask_restful import Resource
from models.Chrompack import Chrompack
from core import defines
from werkzeug.utils import secure_filename


class ResourceChrompack(Resource):

    def __init__(self, **kwargs):

        self._allowed_extensions = ['zip']
        self._upload_dir_chrompack = defines.DATA_CHROMPACK
        self._upload_dir_sample = defines.DATA_SAMPLE

        self._chrompack = Chrompack(kwargs['db_connection'])

    def allowed_file(self, filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in self._allowed_extensions

    def extract_samples(self, filename_zip, id_chrompack):

        sample_list = []
        zf = ZipFile(filename_zip)

        for pos, file in enumerate(zf.namelist()):

            slot = file[-10:-7]  # .rstrip('.ab1')[-6:-3] #[-3:]  #input filename format

            if slot[0] not in 'ABCDEFGH':
                slot = ""

            if slot[1:3] not in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
                slot = ""

            sample = {'filename': file, 'slot': slot}

            self._chrompack.add_sample(sample, id_chrompack)

            filename_extracted = zf.extract(file, self._upload_dir_sample)
            new_filename = "{id}_sample{sample_num}.ab1".format(id=id_chrompack, sample_num=pos)
            new_filename_absolut = self._upload_dir_sample + '/' + new_filename

            os.rename(filename_extracted, new_filename_absolut)
            # p = subprocess.Popen([config.PHREDBIN, sfname, '-pd', config.PHDPOOL],
            #                      env={'PHRED_PARAMETER_FILE': config.PHREDPAR})
            # p.wait()

        return sample_list

    def post(self):

        if 'file' not in request.files:
            return Response('file to upload is not defined', status=400)

        file = request.files['file']
        title_chrompack = request.form.get('title')
        user = 'teste'
        uploaded = datetime.datetime.now()

        if file.filename == '' or not file:
            return Response('file to upload is not defined', status=400)

        if not self.allowed_file(file.filename):
            return Response('file to upload is not zip', status=400)

        if not title_chrompack:
            return Response('title to upload do not be empty', status=400)

        id_chrompack = self._chrompack.save(title_chrompack, user, uploaded)
        file_chrompack = self._chrompack.get_filename(id_chrompack)
        absolut_filename = os.path.join(self._upload_dir_chrompack, file_chrompack)

        file.save(absolut_filename)

        sample_list = self.extract_samples(absolut_filename, id_chrompack)

        self._chrompack.add_sample(sample_list, id_chrompack)

        return Response(status=200)
