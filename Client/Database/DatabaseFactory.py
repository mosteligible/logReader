from abc import ABCMeta
import mysql.connector as ctx
import traceback

from Constants import DB_LOG_LOCATION
from Log import create_logger


class Database:
    def __init__(self, username: str, password: str, host: str, database: str):
        self._username = username
        self._password = password
        self._host = host
        self._connection = None
        self.Reconnect(database=database)
        self.logger = create_logger(
            log_location=DB_LOG_LOCATION, logger_name="DB", file_name="db.log"
        )

    def AddEntry(self, dbPayload: dict, tableName: str) -> bool:
        self.logger.info(f"payload: {dbPayload}")
        insertQuery = f"INSERT INTO {tableName}"
        columnNames = ", ".join([f"`{colName}`" for colName in dbPayload.keys()])
        valuesForColumn = ", ".join(
            [
                "'{}'".format(val.replace("'", "''")) if type(val) == str else f"'{val}'"
                for val in dbPayload.values()
            ]
        )
        query = f"{insertQuery} ({columnNames}) VALUES ({valuesForColumn})"
        self.logger.info(f"Query: {query}")
        try:
            self._cursor.execute(query)
            self._connection.commit()
            self.logger.info(f"Insert query successful")
        except Exception as e:
            self.logger.error(
                f"Insert query for {dbPayload} execution failed with exception {e}\n{traceback.format_exc()}"
            )
            return False
        return True

    def Reconnect(self, database: str):
        if self._connection:
            self._cursor.close()
            self._connection.close()
        self._connection = ctx.connect(
            user=self._username,
            password=self._password,
            host=self._host,
            database=database,
        )
        self._cursor = self._connection.cursor(named_tuple=True)

    def IsConnected(self):
        return self._connection.is_connected()
