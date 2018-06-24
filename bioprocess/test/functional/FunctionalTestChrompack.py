import sys

sys.path.append('core')

import unittest
from datetime import datetime
import requests
import jwt
import defines
from DbConnection import DbConnection


class FunctionalTestChrompack(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = "http://{host}:{port}/chrompack".format(host=defines.BIOPROCESS_HOST, port=defines.BIOPROCESS_PORT)
        cls.db_connection = DbConnection(defines.MONGO_HOST,
                                         defines.MONGO_USER,
                                         defines.MONGO_PASS,
                                         defines.MONGO_DB,
                                         defines.MONGO_PORT)
        cls.collection = 'chrompack'
        cls.user_test = 'test_chrompack_one_sample'

    @classmethod
    def tearDownClass(cls):
        cls.db_connection.remove({'user': cls.user_test}, cls.collection)

    def get_authorization(self, username='test'):
        secret_key = defines.SECRET_KEY
        token = jwt.encode({'username': username}, secret_key).decode()
        return {'Authorization': 'Bearer {}'.format(token)}

    def test_request_without_authorization(self):
        res = requests.post(self.url, {})
        self.assertEqual(res.status_code, 401)

    def test_wrong_token(self):
        secret_key = 'secret key wrong'
        token = jwt.encode({'user': 'test'}, secret_key).decode()
        headers = {'Authorization': 'Bearer {}'.format(token)}

        res = requests.post(self.url, {}, headers=headers)

        self.assertEqual(res.status_code, 422)

    def test_file_empty(self):
        headers = self.get_authorization(self.user_test)
        res = requests.post(self.url, {}, headers=headers)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.text, 'file to upload is not defined')

    def test_file_format_wrong(self):
        headers = self.get_authorization(self.user_test)
        files = {'file': open('test/data/format_wrong.txt', 'rb')}
        res = requests.post(self.url, {}, headers=headers, files=files)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.text, 'file to upload has not correct format')

    # def test_file_invalid(self):
    #     headers = self.get_authorization(self.user_test)
    #     files = {'file': open('test/data/format_wrong.txt', 'rb')}
    #     res = requests.post(self.url, {}, headers=headers, files=files)
    #
    #     self.assertEqual(res.status_code, 400)
    #     self.assertEqual(res.text, 'file to upload has not correct format')

    def test_title_empty(self):
        headers = self.get_authorization(self.user_test)
        files = {'file': open('test/data/test_many_samples.zip', 'rb')}
        res = requests.post(self.url, {}, headers=headers, files=files)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.text, 'title to upload do not be empty')

    def test_upload_chrompack(self):
        files = {'file': open('test/data/test_many_samples.zip', 'rb')}
        headers = self.get_authorization(self.user_test)
        title_test = 'test'
        res = requests.post(self.url, {'title': title_test}, files=files, headers=headers)

        self.assertEqual(res.status_code, 200)

        chrompacks = self.db_connection.find({'user': self.user_test}, self.collection)
        chrompacks = list(chrompacks)

        self.assertEqual(len(chrompacks), 1)

        chrompacks = chrompacks[0]

        self.assertEqual(chrompacks['user'], self.user_test)
        self.assertEqual(chrompacks['title'], title_test)

        today = datetime.now()

        self.assertEqual(chrompacks['uploaded'].day, today.day)
        self.assertEqual(chrompacks['uploaded'].month, today.month)
        self.assertEqual(chrompacks['uploaded'].year, today.year)

        self.assertEqual(len(chrompacks['samples']), 4)

        self.assertEqual(chrompacks['samples'][0]['filename'], 'sample_1.ab1')
        self.assertEqual(chrompacks['samples'][1]['filename'], 'sample_2.ab1')
        self.assertEqual(chrompacks['samples'][2]['filename'], 'sample_3.ab1')
        self.assertEqual(chrompacks['samples'][3]['filename'], 'sample_4.ab1')


if "__main__" == __name__:
    unittest.main()