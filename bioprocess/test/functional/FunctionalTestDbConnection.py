import unittest
from core import defines
from core.DbConnection import DbConnection


class FunctionalTestDbConnection(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.collection = 'collection_test'

    def tearDown(self):
        self.get_instance().remove({}, self.collection)

    def get_instance(self):
        return DbConnection(defines.MONGO_HOST,
                            defines.MONGO_USER,
                            defines.MONGO_PASS,
                            defines.MONGO_DB,
                            defines.MONGO_PORT)

    def test_connect_successful(self):
        self.get_instance()

    def test_insert_and_find(self):
        db_connection = self.get_instance()
        data = {'test': 'test_and_find'}

        db_connection.insert(data, self.collection)
        result = db_connection.find(data, self.collection)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], data)

    def test_delete(self):
        db_connection = self.get_instance()
        data = {'test': 'test_and_find'}

        db_connection.insert(data, self.collection)
        db_connection.remove(data, self.collection)

        result = db_connection.find(data, self.collection)

        self.assertEqual(len(result), 0)

    def test_update(self):
        db_connection = self.get_instance()
        data = {'test': 'test_update'}
        new_data = {'test': 'test_update_ok'}

        db_connection.insert(data, self.collection)
        db_connection.update({'$set': new_data}, data, self.collection)

        result = db_connection.find({}, self.collection)[0]
        del result['_id']

        self.assertEqual(result, new_data)


if __name__ == "__main__":
    unittest.main()