import unittest
import requests
import jwt
from test import test_utils
from core import defines


class FunctionalTestChrompack(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.url = "http://{host}:{port}/chrompack".format(host=defines.BIOPROCESS_HOST,
                                                          port=defines.BIOPROCESS_PORT)

        cls.db_connection = test_utils.get_database_production()

        cls.collection = 'chrompack'
        cls.user_test = 'test_subject_all'

    @classmethod
    def tearDownClass(cls):
        cls.db_connection.remove({'user': cls.user_test}, cls.collection)

    def get_letter_list(self, last_letter):
        code_max_letter = ord(last_letter)
        code_letter_a = ord('A')
        return [chr(letter_code) for letter_code in range(code_letter_a, code_max_letter + 1)]

    def test_request_without_authorization(self):
        url = '{url}/{id}/subject/all'.format(url=self.url, id='5b7091ba8dff0c000ec3eca4')
        res = requests.get(url)
        self.assertEqual(res.status_code, 401)

    def test_wrong_token(self):
        secret_key = 'secret key wrong'
        token = jwt.encode({'user': 'test'}, secret_key).decode()
        headers = {'Authorization': 'Bearer {}'.format(token)}

        url = '{url}/{id}/subject/all'.format(url=self.url, id='5b7091ba8dff0c000ec3eca4')
        res = requests.get(url=url, headers=headers)

        self.assertEqual(res.status_code, 422)

    def test_get_matrix_sucessful(self):
        headers = test_utils.get_authorization(self.user_test)

        with open(test_utils.DATA_TEST_PATH + 'test_many_samples.zip', 'rb') as fp:
            files = {'file': fp}
            title_test = 'test_subject_all_successful'
            res = requests.post(self.url, {'title': title_test}, files=files, headers=headers)

        self.assertEqual(res.status_code, 200)

        url_get_list = '{url}/{endpoint}'.format(url=self.url, endpoint='all')
        res = requests.get(url_get_list, headers=headers)
        res_json = res.json()

        self.assertEqual(len(res_json), 1)

        id_chrompack = res.json()[0]['_id']

        url_subject_all = '{url}/{id}/subject/matrix/all'.format(url=self.url, id=id_chrompack)

        res = requests.get(url_subject_all, headers=headers)

        self.assertEqual(res.status_code, 200)

        matrix = res.json()
        slots_config = test_utils.get_configs_production()['slots']

        lines = list(matrix.keys())
        expected_lines = [str(i) for i in range(1, slots_config['max_position'] + 1)]

        self.assertEqual(lines, expected_lines)

        expected_columns = self.get_letter_list(slots_config['max_letter'])

        for line_index, column in matrix.items():

            keys = list(column.keys())

            self.assertEqual(keys, expected_columns)


if "__main__" == __name__:
    unittest.main()