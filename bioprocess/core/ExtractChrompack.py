import os
from zipfile import ZipFile


class FileInvalid(Exception):
    pass


class ExtractChrompack:

    def __init__(self, chrompack_model):

        self._chrompack_model = chrompack_model

    @staticmethod
    def get_filename(id_chrompack):
        return '{}.zip'.format(id_chrompack)

    def extract_samples(self, filename_zip, user_folder):

        sample_list = []
        zip = ZipFile(filename_zip)
        samples_folder = user_folder + '/samples'

        os.mkdir(samples_folder)

        for pos, file in enumerate(zip.namelist()):

            file_format = file[-3:]

            if file_format != 'ab1':
                raise FileInvalid

            slot = file[-10:-7]

            if slot[0] not in 'ABCDEFGH':
                slot = ""

            if slot[1:3] not in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
                slot = ""

            if slot != "":
                zip.extract(file, samples_folder)
                sample_list.append({'filename': file, 'slot': slot, 'subject': ''})

        return sample_list
