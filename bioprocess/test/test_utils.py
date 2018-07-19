from core import defines
from core.DbConnection import DbConnection


def get_database_production():

    return DbConnection(defines.MONGO_HOST,
                        defines.MONGO_USER,
                        defines.MONGO_PASS,
                        defines.MONGO_DB,
                        defines.MONGO_PORT)