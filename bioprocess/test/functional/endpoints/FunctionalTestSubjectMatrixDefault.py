import unittest
import string
import requests
import jwt
from test import test_utils
from core import defines
from core.slots import SlotState


class FunctionalTestChrompack(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.url = "http://{host}:{port}/subject/matrix/default".format(host=defines.BIOPROCESS_HOST,
                                                                       port=defines.BIOPROCESS_PORT)

        cls.db_connection = test_utils.get_database_production()

        cls.collection = 'chrompack'
        cls.user_test = 'test_subject_matrix_default'

    @classmethod
    def tearDownClass(cls):
        cls.db_connection.remove({'user': cls.user_test}, cls.collection)

    def get_letter_list(self, last_letter):
        letters = list(string.ascii_uppercase)
        index_last_letter = letters.index(last_letter)

        return letters[:index_last_letter + 1]

    def test_request_without_authorization(self):
        res = requests.get(self.url)
        self.assertEqual(res.status_code, 401)

    def test_wrong_token(self):
        secret_key = 'secret key wrong'
        token = jwt.encode({'user': 'test'}, secret_key).decode()
        headers = {'Authorization': 'Bearer {}'.format(token)}

        res = requests.get(url=self.url, headers=headers)

        self.assertEqual(res.status_code, 422)

    def test_get_matrix_default_sucessful(self):
        headers = test_utils.get_authorization(self.user_test)

        res = requests.get(self.url, headers=headers)

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

            for cell in column.values():
                self.assertEqual(cell, SlotState.NOT_FOUND.value)


if "__main__" == __name__:
    unittest.main()