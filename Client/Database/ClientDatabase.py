import traceback
from typing import List, Tuple, Union

from Constants import CLIENT_DB_TABLE_NAME

from .DatabaseFactory import Database


class ClientDatabase(Database):
    def __init__(
        self, username: str, password: str, host: str, database: str, port: int = 3306
    ):
        super().__init__(username, password, host, database, port)

    def AddEntry(self, dbPayload: dict, tableName: str = CLIENT_DB_TABLE_NAME) -> bool:
        return super().AddEntry(dbPayload, tableName)

    def RetreiveClient(
        self, clientId: str, tableName: str = CLIENT_DB_TABLE_NAME
    ) -> Tuple[str, str, str]:
        selectQuery = f"select * from {tableName} where id='{clientId}'"
        try:
            self._cursor.execute(selectQuery)
            self.logger.info(
                f"Successfully retreived client with id {clientId} from {tableName}"
            )
        except Exception as e:
            self.logger.error(
                f"{e} - Error retreiving client with id: {clientId}\n{traceback.format_exc()}"
            )
            return False
        row = self._cursor.fetchall()  # read first row of the fetch from DB
        self._connection.commit()
        if len(row) != 1:
            return False

        return row[0]

    def DeleteClient(self, clientId: str, tableName: str = CLIENT_DB_TABLE_NAME) -> bool:
        deleteQuery = f"delete from `{tableName}` where id='{clientId}'"
        try:
            self._cursor.execute(deleteQuery)
            self.logger.info(
                f"Successfully deleted client with id {clientId} from {tableName}"
            )
        except Exception as e:
            self.logger.error(
                f"{e} - Error retreiving client with id: {clientId}\n{traceback.format_exc()}"
            )
            return False
        return True

    def RetreiveAllClients(
        self, tableName: str = CLIENT_DB_TABLE_NAME
    ) -> Union[List[str], bool]:
        selectAllQuery = f"select * from {tableName}"
        try:
            self._cursor.execute(selectAllQuery)
            self.logger.info("Successfully retreived all clients from DB")
        except Exception as e:
            self.logger.error(
                f"{e} - Error retreiving all data from DB\n{traceback.format_exc()}"
            )
            return False
        clientel = self._cursor.fetchall()
        self._connection.commit()
        return clientel
