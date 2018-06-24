from pymongo import MongoClient
from pymongo.errors import OperationFailure, ServerSelectionTimeoutError


class DbConnection:

    def __init__(self, hostname: str, username: str, password: str, database: str, port: int):

        try:
            client = MongoClient(hostname, port)
            db = client.get_database(database)
            db.authenticate(username, password, mechanism='SCRAM-SHA-1')

            self._conn = db

        except OperationFailure:
            raise ConnectionError("Authentication error")
        except ServerSelectionTimeoutError:
            raise ConnectionError("Timeout error")

    def find(self, data: dict, collection: str):

        if not isinstance(data, dict):
            raise ValueError('filter is not a dict')

        if not isinstance(collection, str):
            raise ValueError('collection is not a string')

        return self._conn.get_collection(collection).find(data)

    def insert(self, data: dict, collection: str):

        if not isinstance(data, dict):
            raise ValueError('filter is not a dict')

        if not isinstance(collection, str):
            raise ValueError('collection is not a string')

        result = self._conn.get_collection(collection).insert_one(data)

        if not result.acknowledged:
            raise Exception('do not possible to insert data')

        return result.inserted_id

    def remove(self, data: dict, collection: str):

        if not isinstance(data, dict):
            raise ValueError('filter is not a dict')

        if not isinstance(collection, str):
            raise ValueError('collection is not a string')

        result = self._conn.get_collection(collection).delete_many(data)

        if not result.acknowledged:
            raise Exception('do not possible to delete data')

    def update(self, data: dict, filter: dict, collection: str):

        if not isinstance(data, dict):
            raise ValueError('data is not a dict')

        if not isinstance(collection, str):
            raise ValueError('collection is not a string')

        if not isinstance(filter, dict):
            raise ValueError('filter is not a string')

        result = self._conn.get_collection(collection).update_one(filter=filter, update=data, upsert=True)

        if not result.acknowledged:
            raise Exception('do not possible to update data')
