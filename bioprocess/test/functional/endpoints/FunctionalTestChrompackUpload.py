import unittest
from datetime import datetime
import requests
import jwt
from test import test_utils
from core import defines


class FunctionalTestChrompack(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = "http://{host}:{port}/chrompack".format(host=defines.BIOPROCESS_HOST, port=defines.BIOPROCESS_PORT)
        cls.db_connection = test_utils.get_database_production()
        cls.collection = 'chrompack'
        cls.user_test = 'test_chrompack_upload'

    @classmethod
    def tearDownClass(cls):
        cls.db_connection.remove({'user': cls.user_test}, cls.collection)

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
        headers = test_utils.get_authorization(self.user_test)
        res = requests.post(self.url, {}, headers=headers)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.text, 'file to upload is not defined')

    def test_file_format_wrong(self):

        with open(test_utils.DATA_TEST_PATH + 'format_wrong.txt', 'rb') as fp:
            headers = test_utils.get_authorization(self.user_test)
            files = {'file': fp}
            res = requests.post(self.url, {}, headers=headers, files=files)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.text, 'file to upload has not correct format')

    def test_file_invalid(self):

        with open(test_utils.DATA_TEST_PATH + 'zip_without_files.zip', 'rb') as fp:
            headers = test_utils.get_authorization(self.user_test)
            files = {'file': fp}
            res = requests.post(self.url, {'title': 'test_file_invalid'}, headers=headers, files=files)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.text, 'the file uploaded is invalid')

    def test_title_empty(self):

        with open(test_utils.DATA_TEST_PATH + 'test_many_samples.zip', 'rb') as fp:
            headers = test_utils.get_authorization(self.user_test)
            files = {'file': fp}
            res = requests.post(self.url, {}, headers=headers, files=files)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.text, 'title to upload do not be empty')

    def test_upload_chrompack(self):

        with open(test_utils.DATA_TEST_PATH + 'test_many_samples.zip', 'rb') as fp:
            files = {'file': fp}
            headers = test_utils.get_authorization(self.user_test)
            title_test = 'test_upload_chrompack'
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

        self.assertEqual(chrompacks['samples'][0]['filename'], '1_A01_01.ab1')
        self.assertEqual(chrompacks['samples'][1]['filename'], '2_B01_03.ab1')
        self.assertEqual(chrompacks['samples'][2]['filename'], '3_C01_05.ab1')
        self.assertEqual(chrompacks['samples'][3]['filename'], '4_D01_07.ab1')


if "__main__" == __name__:
    unittest.main()