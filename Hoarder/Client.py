from time import time
import requests

import Constants
from Exceptions import UserValidationError


class Client:
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
        response = requests.post(validationURL, json=payload)
        response = response.json()
        if response["status"] > 399 or response["token"] == token:
            return False
        return True

    def __repr__(self) -> str:
        return self.id
