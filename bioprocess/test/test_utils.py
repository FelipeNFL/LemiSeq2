import jwt
import json
from core import defines
from core.DbConnection import DbConnection

DATA_TEST_PATH = 'test/data/'


def get_database_production():

    return DbConnection(defines.MONGO_HOST,
                        defines.MONGO_USER,
                        defines.MONGO_PASS,
                        defines.MONGO_DB,
                        defines.MONGO_PORT)


def get_configs_production():

    return get_json_from_file(defines.CONFIG_PATH)


def get_authorization(username):
    secret_key = defines.SECRET_KEY
    token = jwt.encode({'username': username}, secret_key).decode()
    return {'Authorization': 'Bearer {}'.format(token)}


def get_json_from_file(filename):
    with open(filename, 'rb') as fp:
        data = fp.read()
        return json.loads(data)
