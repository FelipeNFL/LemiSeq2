import unittest
from datetime import datetime
from .. import test_utils
from models.Chrompack import Chrompack
from models.User import User


class FunctionalTestUser(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.db = test_utils.get_database_production()
        self.user_test = 'test_functional_user_model'

    def tearDown(self):
        self.db.remove({'user': self.user_test}, 'chrompack')

    def test_get_num_chrompack(self):

        chrompacks = 3

        model_chrompack = Chrompack(self.db)

        for i in range(0, chrompacks):
            model_chrompack.save('title_1', self.user_test, datetime.now())

        model_user = User(self.db, self.user_test)

        self.assertEqual(model_user.get_num_chrompacks(), chrompacks)

    def test_get_samples(self):

        model_chrompack = Chrompack(self.db)

        id_chrompack_1 = model_chrompack.save('title_1', self.user_test, datetime.now())
        id_chrompack_2 = model_chrompack.save('title_1', self.user_test, datetime.now())

        num_samples_each_chrompack = 4

        for i in range(0, num_samples_each_chrompack):
            model_chrompack._add_sample('sample_test', id_chrompack_1)

        for i in range(0, num_samples_each_chrompack):
            model_chrompack._add_sample('sample_test', id_chrompack_2)

        model_user = User(self.db, self.user_test)

        self.assertEqual(model_user.get_num_samples(), num_samples_each_chrompack * 2)

    #TODO fazer testes de contagem de subjects