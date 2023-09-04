import os

import Constants
from Database import ClientDatabase
from dotenv import load_dotenv
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
    port=Constants.CLIENT_DB_PORT,
)

################################
# Box and Hoarder endpoints
################################

BOX_ENDPOINT = os.getenv("BOX_ENDPOINT", "")
isEnvValid(BOX_ENDPOINT, "BOX_ENDPOINT", "")

HOARDER_ENDPOINT = os.getenv("HOARDER_ENDPOINT", "")
isEnvValid(HOARDER_ENDPOINT, "HOARDER_ENDPOINT", "")

# Token to authenticate to add clients to Database
CLIENT_ADD_TOKEN = os.getenv("CLIENT_ADD_TOKEN", "")
isEnvValid(CLIENT_ADD_TOKEN, "CLIENT_ADD_TOKEN", "")

BOX_AUTH_TOKEN = os.getenv("BOX_AUTH_TOKEN", "")
isEnvValid(BOX_AUTH_TOKEN, "BOX_AUTH_TOKEN", "")

HOARDER_AUTH_TOKEN = os.getenv("HOARDER_AUTH_TOKEN", "")
isEnvValid(HOARDER_AUTH_TOKEN, "HOARDER_AUTH_TOKEN", "")
