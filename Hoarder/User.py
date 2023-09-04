from time import time

import Config
import Constants
from Exceptions import UserValidationError
from Log import create_logger
from utils import collectResponse


class User:
    def __init__(self, id: str, token: str, validate=True) -> None:
        self.id = id
        self.token = token
        self.logger = create_logger(
            log_location=Constants.USER_LOG_DIR,
            logger_name=id,
            file_name=f"{id}.log",
        )
        if validate and not self.ValidateClient(id, token):
            raise UserValidationError("Invalid User")
        self._timestamp = time()

    def IsSessionValid(self) -> bool:
        if time() - self._timestamp() > Constants.TIMEOUT_DURATION:
            return False
        return True

    def ValidateClient(self, id: str, token: str) -> bool:
        validationURL = f"{Config.CLIENT_ENDPOINT}/validate"
        payload = {"id": id, "token": token}
        response = collectResponse(url=validationURL, payload=payload)
        if response is None:
            self.logger.info(f"Client Validation for - ID: {id} Failed - token: {token}")
            return False
        self.logger.info(f"response from Client Tracker: {response}")
        statusCode = int(response["status"])
        if statusCode > 399 or response["token"] != token:
            self.logger.info(f"Client Validation for - ID: {id} Failed - token: {token}")
            return False
        self.logger.info(f"Client Validation for - ID: {id} Successful")
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
