from time import time

import Constants
from Exceptions import UserValidationError
from Log import create_logger
from utils import collectResponse


class User:
    def __init__(self, id: str, token: str) -> None:
        self.id = id
        self._token = token
        if not self.ValidateClient(id, token):
            raise UserValidationError("Invalid User")
        self._timestamp = time()

    def IsSessionValid(self) -> bool:
        if time() - self._timestamp() > Constants.TIMEOUT_DURATION:
            return False
        return True

    def ValidateClient(self, id: str, token: str) -> bool:
        validationURL = f"{Constants.CLIENT_ENDPOINT}/validate"
        payload = {"id": id, "token": token}
        response = collectResponse(url=validationURL, payload=payload)
        if response is None:
            return False
        response = response.json()
        if response["status"] > 399 or response["token"] != token:
            return False
        return True

    def __repr__(self) -> str:
        return self.id


# To keep track of clients and log their addition and removal
class Clientels(dict):
    def __init__(self, *args):
        self.logger = create_logger(
            log_location=Constants.CLIENTEL_LOG,
            logger_name="CLIENTEL",
            file_name="clientel.log",
        )
        dict.__init__(self, args)

    def __setitem__(self, key, val):
        self.logger.info(f"Added client:: {key}: {val}")
        dict.__setitem__(self, key, val)
