import os
from dotenv import load_dotenv

import Constants
from Database import ClientDatabase
from Exceptions import EnvironmentVariableError


load_dotenv()


def isEnvValid(var: str, varName: str, default: str) -> bool:
    if var == default:
        raise EnvironmentVariableError(f"{varName} is not set")
    return True


CLIENTDB = ClientDatabase(
    username=Constants.CLIENT_DB_USERNAME,
    password=Constants.CLIENT_DB_PASSWORD,
    host=Constants.CLIENT_DB_HOST,
    database=Constants.CLIENT_DB_NAME,
)

################################
# Box and Hoarder endpoints
################################

BOX_ENDPOINT = os.getenv("BOX_ENDPOINT", "")
isEnvValid(BOX_ENDPOINT, "BOX_ENDPOINT", "")

HOARDER_ENDPOINT = os.getenv("HOARDER_ENDPOINT", "")
isEnvValid(HOARDER_ENDPOINT, "HOARDER_ENDPOINT", "")
