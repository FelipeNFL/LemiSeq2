import os
from zipfile import ZipFile
from datetime import datetime


class FileInvalid(Exception):
    pass


class Chrompack:

    def __init__(self, dbconnection):

        self._dbconnection = dbconnection
        self._collection = 'chrompack'

    def save(self, title, user, uploaded):

        if not isinstance(title, str):
            raise TypeError('desc must be a str, not {}'.format(type(desc)))

        if not isinstance(user, str):
            raise TypeError('user must be a str, not {}'.format(type(user)))

        if not isinstance(uploaded, datetime):
            raise TypeError('uploaded must be a datetime, not {}'.format(type(uploaded)))

        data = {'title': title, 'user': user, 'uploaded': uploaded}

        id_chrompack = self._dbconnection.insert(data, self._collection)

        return id_chrompack

    def _add_sample(self, sample, id_chrompack):
        command_update = {'$push': {'samples': sample}}
        self._dbconnection.update(command_update, {'_id': id_chrompack}, self._collection)

    def delete(self, id_chrompack):
        self._dbconnection.remove({'_id': id_chrompack}, self._collection)

    @staticmethod
    def get_filename(id_chrompack):
        return '{}.zip'.format(id_chrompack)

    def extract_samples(self, filename_zip, id_chrompack, upload_dir):

        sample_list = []
        zf = ZipFile(filename_zip)

        for pos, file in enumerate(zf.namelist()):

            file_format = file[-3:]

            if file_format != 'ab1':
                raise FileInvalid

            slot = file[-10:-7]  # .rstrip('.ab1')[-6:-3] #[-3:]  #input filename format

            if slot[0] not in 'ABCDEFGH':
                slot = ""

            if slot[1:3] not in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
                slot = ""

            sample = {'filename': file, 'slot': slot}

            self._add_sample(sample, id_chrompack)

            filename_extracted = zf.extract(file, upload_dir)
            new_filename = "{id}_sample{sample_num}.ab1".format(id=id_chrompack, sample_num=pos)
            new_filename_absolut = upload_dir + '/' + new_filename

            os.rename(filename_extracted, new_filename_absolut)
            # p = subprocess.Popen([config.PHREDBIN, sfname, '-pd', config.PHDPOOL],
            #                      env={'PHRED_PARAMETER_FILE': config.PHREDPAR})
            # p.wait()

        return sample_list
