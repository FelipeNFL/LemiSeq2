import unittest
from core import defines
from core.DbConnection import DbConnection


class TestDbConnection(unittest.TestCase):

    def get_valid_connection(self):
        return DbConnection(defines.MONGO_HOST,
                            defines.MONGO_USER,
                            defines.MONGO_PASS,
                            defines.MONGO_DB,
                            defines.MONGO_PORT)

    def test_hostname_type_wrong(self):
        with self.assertRaisesRegex(TypeError, "hostname must be a string, not <class 'int'>"):
            DbConnection(123, "username", "password", "database", 123)

    def test_username_type_wrong(self):
        with self.assertRaisesRegex(TypeError, "username must be a string, not <class 'int'>"):
            DbConnection("hostname", 123, "password", "database", 123)

    def test_password_type_wrong(self):
        with self.assertRaisesRegex(TypeError, "password must be a string, not <class 'int'>"):
            DbConnection("hostname", "username", 123, "database", 123)

    def test_database_type_wrong(self):
        with self.assertRaisesRegex(TypeError, "database must be a string, not <class 'int'>"):
            DbConnection("hostname", "username", "password", 123, 123)

    def test_port_type_wrong(self):
        with self.assertRaisesRegex(TypeError, "port must be a int, not <class 'str'>"):
            DbConnection("hostname", "username", "password", "database", "port")

    def test_find_data_type_wrong(self):
        with self.assertRaisesRegex(TypeError, "data must be a dict, not <class 'str'>"):
            self.get_valid_connection().find("data", "collection")

    def test_find_collection_type_wrong(self):
        with self.assertRaisesRegex(TypeError, "collection must be a string, not <class 'int'>"):
            self.get_valid_connection().find({}, 123)

    def test_insert_data_type_wrong(self):
        with self.assertRaisesRegex(TypeError, "data must be a dict, not <class 'str'>"):
            self.get_valid_connection().insert("data", "collection")

    def test_insert_collection_type_wrong(self):
        with self.assertRaisesRegex(TypeError, "collection must be a string, not <class 'int'>"):
            self.get_valid_connection().insert({}, 123)

    def test_remove_data_type_wrong(self):
        with self.assertRaisesRegex(TypeError, "data must be a dict, not <class 'str'>"):
            self.get_valid_connection().remove("data", "collection")

    def test_remove_collection_type_wrong(self):
        with self.assertRaisesRegex(TypeError, "collection must be a string, not <class 'int'>"):
            self.get_valid_connection().remove({}, 123)

    def test_update_data_type_wrong(self):
        with self.assertRaisesRegex(TypeError, "data must be a dict, not <class 'str'>"):
            self.get_valid_connection().update("data", {}, "collection")

    def test_update_collection_type_wrong(self):
        with self.assertRaisesRegex(TypeError, "collection must be a string, not <class 'int'>"):
            self.get_valid_connection().update({}, {}, 123)

    def test_update_filter_type_wrong(self):
        with self.assertRaisesRegex(TypeError, "filter must be a dict, not <class 'str'>"):
            self.get_valid_connection().update({}, "filter", "collection")


if "__main__" == __name__:
    unittest.main()