from pymongo import MongoClient
from pymongo.errors import OperationFailure, ServerSelectionTimeoutError


class DbConnection:

    def __init__(self, hostname: str, username: str, password: str, database: str, port: int):

        if not isinstance(hostname, str):
            raise TypeError('hostname must be a string, not {}'.format(type(hostname)))

        if not isinstance(username, str):
            raise TypeError('username must be a string, not {}'.format(type(username)))

        if not isinstance(password, str):
            raise TypeError('password must be a string, not {}'.format(type(password)))

        if not isinstance(database, str):
            raise TypeError('database must be a string, not {}'.format(type(database)))

        if not isinstance(port, int):
            raise TypeError('port must be a int, not {}'.format(type(hostname)))

        try:
            client = MongoClient(hostname, port)
            db = client.get_database(database)
            db.authenticate(username, password, mechanism='SCRAM-SHA-1')

            self._conn = db

        except OperationFailure:
            raise ConnectionError("Authentication error")
        except ServerSelectionTimeoutError:
            raise ConnectionError("Timeout error")

    def find(self, data: dict, collection: str, fields=None):

        if not isinstance(data, dict):
            raise TypeError('data must be a dict, not {}'.format(type(data)))

        if not isinstance(collection, str):
            raise TypeError('collection must be a string, not {}'.format(type(collection)))

        return list(self._conn.get_collection(collection).find(data, fields))

    def insert(self, data: dict, collection: str):

        if not isinstance(data, dict):
            raise TypeError('data must be a dict, not {}'.format(type(data)))

        if not isinstance(collection, str):
            raise TypeError('collection must be a string, not {}'.format(type(collection)))

        result = self._conn.get_collection(collection).insert_one(data)

        if not result.acknowledged:
            raise Exception('do not possible to insert data')

        return result.inserted_id

    def remove(self, data: dict, collection: str):

        if not isinstance(data, dict):
            raise TypeError('data must be a dict, not {}'.format(type(data)))

        if not isinstance(collection, str):
            raise TypeError('collection must be a string, not {}'.format(type(collection)))

        result = self._conn.get_collection(collection).delete_many(data)

        return result.deleted_count

    def update(self, data: dict, _filter: dict, collection: str):

        if not isinstance(data, dict):
            raise TypeError('data must be a dict, not {}'.format(type(data)))

        if not isinstance(_filter, dict):
            raise TypeError('filter must be a dict, not {}'.format(type(_filter)))

        if not isinstance(collection, str):
            raise TypeError('collection must be a string, not {}'.format(type(collection)))

        result = self._conn.get_collection(collection).update_one(filter=_filter, update=data, upsert=True)

        import logging
        logging.info('update')
        logging.info(result)

        if not result.acknowledged:
            raise Exception('do not possible to update data')
