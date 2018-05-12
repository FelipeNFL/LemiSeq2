import MySQLdb


class DbConnectionMySQL:

    def __init__(self, host: str, port: int, user: str, password: str, database: str):

        self._host = host
        self._port = port
        self._user = user
        self._password = password
        self._database = database

        self._connection = MySQLdb.connect(host=self._host,
                                           user=self._user,
                                           passwd=self._password,
                                           db=self._database,
                                           port=self._port)

    def command_without_return(self, command: str, params: list):
        pass
