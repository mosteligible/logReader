from typing import Dict, Tuple
from Constants import CLIENT_DB_TABLE_NAME
from .DatabaseFactory import Database


class ClientDatabase(Database):
    def __init__(self, username: str, password: str, host: str, database: str):
        super().__init__(username, password, host, database)

    def RetreiveClient(self, clientId: str) -> Tuple[str, str, str]:
        selectQuery = f"select * from {CLIENT_DB_TABLE_NAME} where id='{clientId}'"
        try:
            self._cursor.execute(selectQuery)
            self.logger.info(
                f"Successfully added client with id {clientId} from {CLIENT_DB_TABLE_NAME}"
            )
        except Exception as e:
            self.logger.error(f"Error retreiving client with id: {clientId}")
            return False
        return self._cursor.fetchall()

    def DeleteClient(self, clientId: str) -> bool:
        deleteQuery = f"delete from `{CLIENT_DB_TABLE_NAME}` where id='{clientId}'"
        try:
            self._cursor.execute(deleteQuery)
            self.logger.info(
                f"Successfully deleted client with id {clientId} from {CLIENT_DB_TABLE_NAME}"
            )
        except Exception as e:
            self.logger.error(f"Error retreiving client with id: {clientId}")
            return False
        return True
