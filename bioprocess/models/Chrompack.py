from bson.objectid import ObjectId
from datetime import datetime


#TODO precisa testar essa classe
class Chrompack:

    def __init__(self, dbconnection):

        self._dbconnection = dbconnection
        self._collection = 'chrompack'

    def save(self, title, user, uploaded):

        if not isinstance(title, str):
            raise TypeError('desc must be a str, not {}'.format(type(title)))

        if not isinstance(user, str):
            raise TypeError('user must be a str, not {}'.format(type(user)))

        if not isinstance(uploaded, datetime):
            raise TypeError('uploaded must be a datetime, not {}'.format(type(uploaded)))

        data = {'title': title, 'user': user, 'uploaded': uploaded}

        id_chrompack = self._dbconnection.insert(data, self._collection)

        return str(id_chrompack)

    def _add_sample(self, sample, id_chrompack):
        command_update = {'$push': {'samples': sample}}
        self._dbconnection.update(command_update, {'_id': id_chrompack}, self._collection)

    def delete(self, id):
        return self._dbconnection.remove({'_id': ObjectId(id)}, self._collection)

    def add_subject(self, name, id_chrompack):
        command_update = {'$push': {'subjects': name}}
        self._dbconnection.update(command_update, {'_id': ObjectId(id_chrompack)}, self._collection)

    def get_subjects_by_id(self, id_chrompack):

        data = self._dbconnection.find({'_id': ObjectId(id_chrompack)}, self._collection, {'subjects': 1})[0]

        if 'subjects' in data:
            return data['subjects']

        return []

    def get_list(self, username):
        return self._dbconnection.find({'user': username}, self._collection, {'_id': 1, 'title': 1})

    def get_samples_by_id(self, id):

        data = self._dbconnection.find({'_id': ObjectId(id)}, self._collection, {'samples': 1})

        if not len(data):
            return None

        data = data[0]

        if 'samples' in data:
            return data['samples']

        return None

    def update_all_samples(self, id_chrompack, samples):
        command_update = {'$set': {'samples': samples}}
        return self._dbconnection.update(command_update, {'_id': ObjectId(id_chrompack)}, self._collection)
