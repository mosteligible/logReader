from typing import Dict, Tuple
from Constants import CLIENT_DB_TABLE_NAME
from .DatabaseFactory import Database


class ClientDatabase(Database):
    def __init__(self, username: str, password: str, host: str, database: str):
        super().__init__(username, password, host, database)
    
    def AddEntry(self, dbPayload: dict, tableName: str = CLIENT_DB_TABLE_NAME) -> bool:
        return super().AddEntry(dbPayload, tableName)

    def RetreiveClient(self, clientId: str) -> Tuple[str, str, str]:
        selectQuery = f"select * from {CLIENT_DB_TABLE_NAME} where id='{clientId}'"
        try:
            self._cursor.execute(selectQuery)
            self.logger.info(
                f"Successfully retreived client with id {clientId} from {CLIENT_DB_TABLE_NAME}"
            )
        except Exception as e:
            self.logger.error(f"Error retreiving client with id: {clientId}")
            return False
        row = self._cursor.fetchall()  # read first row of the fetch from DB
        if len(row) != 1:
            return False
        
        return tuple(row[0])

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
