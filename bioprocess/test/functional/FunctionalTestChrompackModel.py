import unittest
from models.Chrompack import Chrompack
from test import test_utils


class FunctionalTestChrompack(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.db_connection = test_utils.get_database_production()

    def test_get_samples_by_id_when_id_not_exists(self):

        model = Chrompack(self.db_connection)
        model._collection = 'chrompack_test'

        self.assertIsNone(model.get_samples_by_id('5b70cc088dff0c000e3425d6'))


if __name__ == "__main__":
    unittest.main()
