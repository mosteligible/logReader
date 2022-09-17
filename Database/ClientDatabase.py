from typing import Tuple
from Constants import CLIENT_DB_TABLE_NAME
from .DatabaseFactory import Database


class ClientDatabase(Database):
    def __init__(self, username: str, password: str, host: str, database: str):
        super().__init__(username, password, host, database)

    def RetreiveClient(self, clientId: str) -> Tuple[str, str, str]:
        selectQuery = f"select * from {CLIENT_DB_TABLE_NAME} where id='{clientId}'"
        self._cursor.execute(selectQuery)
        return self._cursor.fetchall()
