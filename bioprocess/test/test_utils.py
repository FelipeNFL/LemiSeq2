import jwt
from core import defines
from core.DbConnection import DbConnection


def get_database_production():

    return DbConnection(defines.MONGO_HOST,
                        defines.MONGO_USER,
                        defines.MONGO_PASS,
                        defines.MONGO_DB,
                        defines.MONGO_PORT)


def get_authorization(username):
    secret_key = defines.SECRET_KEY
    token = jwt.encode({'username': username}, secret_key).decode()
    return {'Authorization': 'Bearer {}'.format(token)}