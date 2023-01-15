from clientUtils import isPlanValid
from Config import CLIENTDB
from Constants import CLIENT_DB_TABLE_NAME, CLIENT_LOG_LOCATION
from Log import create_logger


class Client:
    def __init__(self, name: str, id: str, ip: str, plan: str) -> None:
        """
        :params:
            name (string): Name of client
            id (string): unique id associated with client. It will be primary key
                         for client.
            plan (string): log storage plan for client. It can be one of `small`,
                           `medium` and `large`
        """
        isPlanValid(plan.lower())
        self.name = name.capitalize()
        self.id = id
        self.ip = ip
        self.plan = plan.capitalize()
        self.logger = create_logger(
            log_location=CLIENT_LOG_LOCATION,
            logger_name="CLIENT",
            file_name=f"{id}.log",
        )

    def AddClient(self) -> bool:
        """
        Adds client to the DB
        """
        payload = {"id": self.id, "name": self.name, "ip": self.ip, "plan": self.plan}
        try:
            CLIENTDB.AddEntry(payload, tableName=CLIENT_DB_TABLE_NAME)
        except Exception as e:
            self.logger.error(
                f"Error- {e} - Could not add client {self.name} with id {self.id}"
            )
            return False

        self.logger.info(f"Successfully added Client {self.name} with id {self.id}")
        return True

    def RemoveClient(self) -> bool:
        """
        Deletes client from DB
        """
        return CLIENTDB.DeleteClient(self.id)
