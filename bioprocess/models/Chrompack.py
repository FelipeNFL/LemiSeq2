from datetime import datetime


class Chrompack:

    def __init__(self, dbconnection):

        self._dbconnection = dbconnection
        self._collection = 'chrompack'

    def save(self, desc, user, uploaded):

        if not isinstance(desc, str):
            raise TypeError('desc must be a str, not {}'.format(type(desc)))

        if not isinstance(user, str):
            raise TypeError('user must be a str, not {}'.format(type(user)))

        if not isinstance(uploaded, datetime):
            raise TypeError('uploaded must be a datetime, not {}'.format(type(uploaded)))

        data = {'desc': desc, 'user': user, 'uploaded': uploaded}

        id_chrompack = self._dbconnection.insert(data, self._collection)

        return id_chrompack

    def add_sample(self, sample, id_chrompack):
        command_update = {'$push': {'samples': sample}}
        self._dbconnection.update(command_update, {'_id': id_chrompack}, self._collection)

    @staticmethod
    def get_filename(id_chrompack):
        return '{}.zip'.format(id_chrompack)
